# https://djbook.ru/rel1.8/howto/custom-management-commands.html
from django.core.management.base import BaseCommand, CommandError
from commandapp.models import Section, Division, Party, Deputy, Roles, Commissions, \
        Members, Address, ReceptionSchedule, Assistants
import csv
from datetime import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('========== Заполнение базы данных ==========')

        print('====== Заполнение таблицы Section ==========')
        with open('content/1_Section.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                Section.objects.create(name=row[0])
                print(row[0])
        print('=============================================')
        print()
        print('====== Заполнение таблицы Division ==========')
        with open('content/2_Division.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                Division.objects.create(name=row[0], number=int(row[1]))
                print(row[0], row[1])
        print('=============================================')
        print()
        print('====== Заполнение таблицы Party =============')
        with open('content/3_Party.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                Party.objects.create(name=row[0], propose_name=row[1], member_name=row[2])
                print(row[0])
        print('=============================================')
        print()
        print('====== Заполнение таблицы Roles =============')
        with open('content/4_Roles.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                Roles.objects.create(name=row[0])
                print(row[0])
        print('=============================================')
        print()
        print('====== Заполнение таблицы Commissions =============')
        with open('content/5_Commissions.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                Commissions.objects.create(name=row[0], description=row[1])
                print(row[0])
        print('=============================================')
        print()
        print('====== Заполнение таблицы Address =============')
        with open('content/6_Address.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                Address.objects.create(name=row[0], full_address=row[1], address=row[2])
                print(row[0])
        print('=============================================')

        print()
        print('====== Заполнение таблицы Deputy =============')
        with open('content/7_Deputy.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for i, row in enumerate(reader):
                if i > 0:       # В первой строке заколовки колонок - пропускаем
                    party = Party.objects.get(name=row[13])
                    division = Division.objects.get(number=row[14])
                    if len(row[3]) > 0:
                        Deputy.objects.create(surname=row[0], name=row[1], second_name=row[2],
                                              date_of_birth=datetime.strptime(row[3], "%Y-%m-%d").date(),
                                              address=row[4], site=row[5], telephone=row[6], email=row[7],
                                              skype=row[8], telegram=row[9], is_head=row[10], is_party=row[11],
                                              is_man=row[12], party_propose=party, division=division)
                    else:
                        Deputy.objects.create(surname=row[0], name=row[1], second_name=row[2],
                                              address=row[4], site=row[5], telephone=row[6], email=row[7],
                                              skype=row[8], telegram=row[9], is_head=row[10], is_party=row[11],
                                              is_man=row[12], party_propose=party, division=division)
                    print(row[0], row[1], row[2], row[3])

        # surname | name | second_name | date_of_birth | address | site | telephone | email | skype | telegram |
        # is_head | is_party | is_man | party_propose | division
        print('=============================================')

        print()
        print('=== Заполнение таблицы Members ====')
        with open('content/8_Members.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                deputy = Deputy.objects.get(surname=row[0])
                commissions = Commissions.objects.get(name=row[1])
                role = Roles.objects.get(name=row[2])

                Members.objects.create(deputy=deputy, role=role, commissions=commissions)
                print(row[0], row[1], row[2])
        print('=============================================')

        print()
        print('=== Заполнение таблицы ReceptionSchedule ====')
        with open('content/9_Schedule.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                deputy = Deputy.objects.get(surname=row[0])
                address = Address.objects.get(name=row[4])
                start = datetime.strptime(row[2], "%H:%M").time()
                end = datetime.strptime(row[3], "%H:%M").time()
                ReceptionSchedule.objects.create(date=datetime.strptime(row[1], "%Y-%m-%d").date(),
                                                 start_time=start, end_time=end, deputy=deputy,
                                                 address=address)
                print(row[0], row[1], row[2], row[3], row[4])
        print('=============================================')

        print()
        print('=== Заполнение таблицы Assistants ====')
        with open('content/10_Assistants.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                deputy = Deputy.objects.get(surname=row[0])
                Assistants.objects.create(surname=row[1], name=row[2], second_name=row[3], deputy=deputy)
                print(row[0], row[1], row[2], row[3])
        print('=============================================')


