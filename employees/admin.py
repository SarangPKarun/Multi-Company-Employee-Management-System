from django.contrib import admin
from .models import Emp

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'emp_id', 'phone', 'department', 'working')
    search_fields = ('name', 'emp_id')
    list_filter = ('working', 'department')

admin.site.register(Emp, EmpAdmin)
