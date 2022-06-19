from django.db import models


class DizaynerskoeVoznagrazhdenie(models.Model):
    class Meta:
        db_table = "dizaynerskoe_voznagrazhdenie_akcii"
        verbose_name = 'Дизайнерское вознагрождение'
        verbose_name_plural = 'Дизайнерское вознагрождение'

    nazvanie_akcii = models.CharField(unique=True, max_length=200, default='', verbose_name="Название акциий")
    aktivnost = models.BooleanField(default=True, verbose_name="Активно/Нет")

    def __str__(self):
        return self.nazvanie_akcii
