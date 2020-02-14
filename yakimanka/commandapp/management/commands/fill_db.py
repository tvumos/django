# https://djbook.ru/rel1.8/howto/custom-management-commands.html
from django.core.management.base import BaseCommand, CommandError
from commandapp.models import Section, Roles, Commissions, Employee, Members


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('fill_db')