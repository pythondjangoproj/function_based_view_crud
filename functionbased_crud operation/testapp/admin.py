from django.contrib import admin
from testapp.models import employee
# Register your models here.

class employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']

admin.site.register(employee,employeeadmin)
