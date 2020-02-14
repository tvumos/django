from django.contrib import admin
from .models import Employee, Commissions, Members, Roles, Section

# Register your models here.

admin.site.register(Employee)
admin.site.register(Commissions)
admin.site.register(Members)
admin.site.register(Roles)
admin.site.register(Section)
