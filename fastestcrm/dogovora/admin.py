from django.contrib import admin


# Register your models here.
from dogovora.models import Dogovor, DizaynerskoeVoznagrazhdenie


class DogovorAdmin(admin.ModelAdmin):
    list_display = ['tip_dogovora', 'nomer_dogovora', 'froze', 'author', 'published']
    list_filter = ['tip_dogovora', ]    # для поиска договоров по типам договоров.


class DizaynerskoeVoznagrazhdenieAdmin(admin.ModelAdmin):
    list_display = ['nazvanie_akcii', 'aktivnost']


admin.site.register(Dogovor, DogovorAdmin)
admin.site.register(DizaynerskoeVoznagrazhdenie, DizaynerskoeVoznagrazhdenieAdmin)

