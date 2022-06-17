from django.db import models
from django.contrib.auth.models import User

from inquery.models import Inquery
from inquery.managers import InqueryStatusManager


class InqueryStatus(models.Model):
    """Статус заявки"""
    froze = models.ForeignKey(Inquery, on_delete=models.CASCADE, verbose_name="Заявка")
    call_back = models.DateField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True, verbose_name="Дата замера")
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=Inquery.INQUERY_STATUS_CHOICES, verbose_name="Статус")
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name="Дата изменения")
    hidden = models.BooleanField(default=False, verbose_name="Заявка скрыта/активна")
    actual = models.BooleanField(default=True)

    objects = models.Manager()
    manager = InqueryStatusManager()

    def __unicode__(self):
        return u"{0} {1} {2}".format(self.froze, self.status, self.created_at)

    class Meta:
        default_permissions = []
        verbose_name = 'Статус заявки'
        verbose_name_plural = 'Статусы заявок'
