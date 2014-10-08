from django.shortcuts import render
from models import Day
import parser as pr

def index(request):
	if pr.should_update():
		pr.update()
	days = Day.objects.order_by('date')
	return render(request,'index.html',{"days":days})