# https://djbook.ru/rel1.8/howto/custom-management-commands.html
from django.core.management.base import BaseCommand, CommandError
from commandapp.models import Section, Division, Party, Deputy, Roles, Commissions, \
        Members, Address, ReceptionSchedule, Assistants


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('===== Вывод записей в таблице Section =======')
        sections = Section.objects.all()
        for section in sections:
            print(section)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице Division =======')
        divisions = Division.objects.all()
        for division in divisions:
            print(division)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице Party =======')
        partyes = Party.objects.all()
        for party in partyes:
            print(party)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице Roles =======')
        roles = Roles.objects.all()
        for role in roles:
            print(role)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице Commissions =======')
        commissions = Commissions.objects.all()
        for comm in commissions:
            print(comm)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице Address =======')
        address = Address.objects.all()
        for add in address:
            print(add)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице Deputy =======')
        deputyes = Deputy.objects.all()
        for deputy in deputyes:
            print(deputy)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице ReceptionSchedule =======')
        reception_schedules = ReceptionSchedule.objects.all()
        for schedule in reception_schedules:
            print(schedule)
        print('=============================================')
        print()
        print('===== Вывод записей в таблице Assistants =======')
        assistants = Assistants.objects.all()
        for assistant in assistants:
            print(assistant)
        print('=============================================')


