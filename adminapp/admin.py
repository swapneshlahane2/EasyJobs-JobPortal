from django.contrib import admin
from adminapp.models import Address, ITJobs, MechJobs, CivilJobs
# Register your models here.

admin.site.register(ITJobs)

admin.site.register(Address)

admin.site.register(MechJobs)

admin.site.register(CivilJobs)
