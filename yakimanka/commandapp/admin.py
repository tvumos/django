from django.contrib import admin
from .models import Section, Division, Party, Deputy, Roles, Commissions, \
        Members, Address, ReceptionSchedule, Assistants


admin.site.register(Division)
admin.site.register(Party)
admin.site.register(Address)
admin.site.register(ReceptionSchedule)
admin.site.register(Assistants)
admin.site.register(Deputy)
admin.site.register(Commissions)
admin.site.register(Members)
admin.site.register(Roles)
admin.site.register(Section)
