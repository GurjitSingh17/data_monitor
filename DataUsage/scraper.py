from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date as Date
from models import Day


user = 'your youser name here'
pwd = 'pass here '
host = '192.168.1.1'
url = 'http://' + user + ":" + pwd + "@" + host + '/Main_TrafficMonitor_daily.asp'


def update():
	browser= webdriver.PhantomJS(executable_path = "path to PhantomJS")
	browser.get(url)

	html = browser.page_source
	browser.close()

	content = BeautifulSoup(html, 'html5lib')
	usage = {}
	if len(content.find_all(id="bwm-daily-grid")) == 0:
		## exit if content not found or connection error
		return False
	for row in content.find_all(id="bwm-daily-grid")[0].find_all("tr"):
		if len(row.find_all(class_="total")) == 0:
			continue ##skip header rows or rows not containing data
		date  = str(row.find_all(class_="rtitle")[0].text)
		dl    = float((str(row.find_all(class_="dl")[0].text)).split(" ")[0])
		ul    = float((str(row.find_all(class_="ul")[0].text)).split(" ")[0])
		total = float((str(row.find_all(class_="total")[0].text)).split(" ")[0])
		usage[date] = {"download":dl,"upload":ul,"total":total}

		objs= Day.objects.all().filter(date=date)
		if (len(objs) > 0):
			obj = objs[0]
			if (obj.download != dl or obj.upload != ul or obj.total != total):
				obj.download = dl
				obj.upload= ul
				obj.total = total
				obj.save()
		else:
			obj= Day(download=dl,upload=ul,total=total,date=date)
			obj.save()
	return True

def time_stamp(date=datetime.now()):
	if (type(date) == str):
		##add leading 0's
		date = date.split("-")
		date = [int(i) for i in date]
		return '{0:02d}-{1:02d}-{2:02d}'.format(date[0],date[1],date[2])
	else:
		return Date.today().isoformat()

def should_update():
	##update if today is not in the database
	today = time_stamp()
	if(Day.objects.all().filter(date=today).exists()):
		return False
	else:
		return True

