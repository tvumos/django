from django.db import models

# Create your models here.


class Section(models.Model):
    """
    Секции/Разделы сайта
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        print(f'{self.name}')


class Employee(models.Model):
    surname = models.CharField(max_length=255, null=False)
    name = models.CharField(max_length=100, null=False)
    second_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255)
    site = models.URLField()
    telephone = models.CharField(max_length=30)
    email = models.EmailField()
    # photo = models.ImageField()

    def __str__(self):
        print(f'{self.surname} {self.surname} {self.second_name}')


class Roles(models.Model):
    name = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)

    def __str__(self):
        print(f'{self.name}')


class Commissions(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        print(f'{self.name}')


class Members(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE)
    commissions = models.ForeignKey(Commissions, on_delete=models.CASCADE)

    def __str__(self):
        print(f'{self.employee} {self.role} {self.commissions}')









