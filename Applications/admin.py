from django.contrib import admin

from .models import Application
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['First_Name', 'Last_Name', 'Email']
    
admin.site.register(Application, EmployeeAdmin)