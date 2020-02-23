from django.core.management.base import BaseCommand, CommandError
from commandapp.models import Section, Division, Party, Deputy, Roles, Commissions, \
        Members, Address, ReceptionSchedule, Assistants
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('==== Удаление записей в таблице Section =====')
        Section.objects.all().delete()
        print('Записи в таблице Section удалены')
        print('=============================================')

        print('==== Удаление записей в таблице Division =====')
        Division.objects.all().delete()
        print('Записи в таблице Division удалены')
        print('=============================================')

        print('==== Удаление записей в таблице Party =====')
        Party.objects.all().delete()
        print('Записи в таблице Party удалены')
        print('=============================================')

        print('==== Удаление записей в таблице Roles =====')
        Roles.objects.all().delete()
        print('Записи в таблице Roles удалены')
        print('=============================================')

        print('==== Удаление записей в таблице Commissions =====')
        Commissions.objects.all().delete()
        print('Записи в таблице Commissions удалены')
        print('=============================================')

        print('==== Удаление записей в таблице Address =====')
        Address.objects.all().delete()
        print('Записи в таблице Address удалены')
        print('=============================================')

        print('==== Удаление записей в таблице Deputy =====')
        Deputy.objects.all().delete()
        print('Записи в таблице Deputy удалены')
        print('=============================================')

        print('Остальные таблицы очищены каскадно')
