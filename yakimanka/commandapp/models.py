from django.db import models


class Section(models.Model):
    """
    Секции/Разделы сайта
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Division(models.Model):
    """
    Справочник избирательных округов
    """
    name = models.CharField(max_length=255, unique=True)
    number = models.IntegerField()

    def __str__(self):
        return f'{self.name}; №{self.number}'


class Party(models.Model):
    """
    Таблица партий
    name            - Наименование партии
    propose_name    - Партия выдвинувшая кандидата в депутаты
    member_name     - Членство в партии
    """
    name = models.CharField(max_length=255, unique=True)
    propose_name = models.CharField(max_length=255)
    member_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class Deputy(models.Model):
    """
    Справочник депутатов совета депутатов
    """
    surname = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True)
    address = models.CharField(max_length=255)
    site = models.URLField()
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    skype = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    is_head = models.BooleanField()
    is_party = models.BooleanField()
    is_man = models.BooleanField()
    party_propose = models.ForeignKey(Party, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    # photo = models.ImageField()

    def __str__(self):
        return f'{self.surname} {self.name} {self.second_name}'


class Roles(models.Model):
    """
    Справочник ролей в совете депутатов
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}'


class Commissions(models.Model):
    """
    Список комиссий созданных в совете депутатов
    """
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'


class Members(models.Model):
    """
    Таблица соответствия сотрудника, его роли и ссылки на комиссию
    """
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    commissions = models.ForeignKey(Commissions, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.deputy} {self.role} {self.commissions}'


class Address(models.Model):
    """
    Справочник адресов помещений для приема депутатов
    """
    name = models.CharField(max_length=255)
    full_address = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class ReceptionSchedule(models.Model):
    """
    Таблица с расписанием приёма граждан депутатами МО Якиманка
    """
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date} с:{self.start_time} по:{self.end_time} {self.deputy}'


class Assistants(models.Model):
    surname = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100)
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE)
    # photo = models.ImageField()

    def __str__(self):
        return f'{self.surname} {self.name} {self.second_name} помошник депутата:{self.deputy}'


