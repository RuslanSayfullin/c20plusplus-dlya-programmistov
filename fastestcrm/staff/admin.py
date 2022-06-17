from django.contrib import admin

from staff.models import Staff


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'departament')
    list_filter = ('departament', )
