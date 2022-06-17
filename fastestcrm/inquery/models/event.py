from datetime import timezone, datetime

from django.db import models
from django.contrib.auth.models import User

from inquery.managers import BusyManager


class Event(models.Model):
    owner = models.ForeignKey(User, related_name='event_owner', on_delete=models.CASCADE)
    designer = models.ForeignKey(User, related_name='event_designer', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    all_day = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    canceled = models.BooleanField(default=False)

    objects = models.Manager()
    busy_manager = BusyManager()

    class Meta:
        default_permissions = []

    def is_past(self):
        now = timezone.now()
        date_now = datetime.date(now.year, now.month, now.day)
        start_date = datetime.date(self.start_datetime.year, self.start_datetime.month, self.start_datetime.day)
        if date_now > start_date:
            return True
        return False

    def get_full_name(self):
        """Используется при выгрузке Графиков работ"""
        return self.designer.get_full_name()
