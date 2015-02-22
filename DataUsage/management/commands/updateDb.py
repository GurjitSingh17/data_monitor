from django.core.management.base import NoArgsCommand
from django.conf import settings
import DataUsage.parser as pr


class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        pr.update()