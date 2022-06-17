import random

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from inquery.api import is_day_weekend
from .managers import KOManager

User = settings.AUTH_USER_MODEL


class Staff(models.Model):
    DEPARTAMENT_KO = 0
    DEPARTAMENT_SUPERVISOR_KO = 1
    DEPARTAMENT_TZ = 2
    DEPARTAMENT_CC = 3
    DEPARTAMENT_VD = 4
    DEPARTAMENT_SDM = 5
    DEPARTAMENT_SDP = 6
    DEPARTAMENT_SDE = 7
    DEPARTAMENT_SDB = 8
    DEPARTAMENT_VDB = 9
    DEPARTAMENT_KOO = 10
    DEPARTAMENT_OFI = 11
    DEPARTAMENT_MOS = 12
    DEPARTAMENT_SEW = 13

    DEPARTAMENT_CHOICE = (
        (DEPARTAMENT_KO, u"Конструкторский отдел"),
        (DEPARTAMENT_SUPERVISOR_KO, u"Администратор конструкторского отдела | ТЗ"),
        (DEPARTAMENT_TZ, u"Технический замер"),
        (DEPARTAMENT_CC, u"Кол центр"),
        (DEPARTAMENT_VD, u"Выездные дизайнеры"),
        (DEPARTAMENT_SDM, u"Салон дизайнеры на Менделеева"),
        (DEPARTAMENT_SDP, u"Салон дизайнеры на Проспекте"),
        (DEPARTAMENT_SDE, u"Салон дизайнеры на Энтузиастов"),
        (DEPARTAMENT_SDB, u"Руководитель салон-дизайнеров"),
        (DEPARTAMENT_VDB, u"Руководитель выездных дизайнеров"),
        (DEPARTAMENT_KOO, u"Конструкторский отдел - остальные"),
        (DEPARTAMENT_OFI, u"Дизайнеры Офис"),
        (DEPARTAMENT_MOS, u"Дизайнеры Москва"),
        (DEPARTAMENT_SEW, u"Швейный цех"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Сотрудник")
    phone = models.CharField(u"Рабочий телефон", max_length=20, null=True, blank=True, help_text=u"используется в sms оповещения, формат 89123456789")
    departament = models.SmallIntegerField(choices=DEPARTAMENT_CHOICE, null=True, blank=True, verbose_name="Отдел")
    is_locking = models.BooleanField(default=False, help_text=u"Пользователь заблокирован на время, он можете входить, но не может получать новые замеры")

    objects = models.Manager()
    manager_ko = KOManager()

    @classmethod
    def active_today_ko(cls, today_date):
        qs = cls.manager_ko.active()
        staff_ko_active_today = [staff_ko for staff_ko in qs if not is_day_weekend(staff_ko.user, today_date)]
        return random.choice(staff_ko_active_today)

    @classmethod
    def _is_departament(cls, user, departament_choice):
        try:
            return user.staff.departament == departament_choice
        except ObjectDoesNotExist:
            return False

    @classmethod
    def is_departament_ko(cls, user):
        return cls._is_departament(user, cls.DEPARTAMENT_KO)

    @classmethod
    def is_departament_supervisor_ko(cls, user):
        return cls._is_departament(user, cls.DEPARTAMENT_SUPERVISOR_KO)

    def get_full_name(self):
        return self.user.get_full_name()

    def get_staff_title(self):
        for dep in self.DEPARTAMENT_CHOICE:
            if dep[0] == self.departament:
                return dep[1]

    class Meta:
        ordering = ("user",)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
