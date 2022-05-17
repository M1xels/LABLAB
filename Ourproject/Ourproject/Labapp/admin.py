from django.contrib import admin
 #index #homepage, hardware_reports, software_reports
from .models import index, register1, homepage, hardware_reports, software_reports

# Register your models here.
admin.site.register(register1)
admin.site.register(index)

