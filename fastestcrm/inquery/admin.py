from django.contrib import admin

from inquery.models.client import Client
from inquery.models.inquery import Inquery
from inquery.models.inqueryfile import InqueryFile
from inquery.models.inquerystatus import InqueryStatus


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')  # Поля, которые отображаются в панели администратора
    list_display_links = ('id', 'name')  # Поля, которые открывают заявку в панели администратора
    search_fields = ('id', 'name',)  # Поля, по которым можно выполнять поиск


class InqueryAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'designer', 'client',
                    'type_production', 'description',
                    'source', 'created_at', 'status',)    # Поля, которые отображаются в панели администратора
    list_display_links = ('id', 'client')   # Поля, которые открывают заявку в панели администратора
    search_fields = ('id', 'uuid',)     # Поля, по которым можно выполнять пойск


class InqueryFileAdmin(admin.ModelAdmin):
    list_display = ['froze_status', 'name', 'path', 'created_at']


class InqueryStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'froze', 'status', 'author',
                    'created_at', 'updated_at',
                    'start_datetime', 'hidden')    # Поля, которые отображаются в панели администратора
    list_display_links = ('id', 'froze')   # Поля, которые открывают заявку в панели администратора
    search_fields = ('id', 'froze')     # Поля, по которым можно выполнять пойск


admin.site.register(Client, ClientAdmin)
admin.site.register(Inquery, InqueryAdmin)
admin.site.register(InqueryFile, InqueryFileAdmin)
admin.site.register(InqueryStatus, InqueryStatusAdmin)
