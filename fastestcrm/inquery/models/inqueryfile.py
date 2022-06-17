import base64
import os

from django.db import models

from inquery.managers import InqueryFileManager

from .inquerystatus import InqueryStatus


class InqueryFile(models.Model):
    froze_status = models.ForeignKey(InqueryStatus, on_delete=models.CASCADE, verbose_name="Статус заявки")
    name = models.CharField(max_length=255, verbose_name="Название файла")
    path = models.CharField(max_length=255, verbose_name="Путь к файлу")
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Дата создания")
    is_delete = models.BooleanField(default=False)

    objects = InqueryFileManager()

    class Meta:
        default_permissions = []
        verbose_name = 'Файл заявки'
        verbose_name_plural = 'Файлы заявок'

    def get_absolute_url(self):
        path, filename = os.path.split(self.path)
        return "https://portal-re-formaufa.ru/media/{0}".format(filename)  # fixme: not use absolute url

    def read(self):
        with open(self.path) as fd:
            return base64.b64encode(fd.read())
