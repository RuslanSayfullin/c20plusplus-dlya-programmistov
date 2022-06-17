import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class InqueryManager(models.Manager):
    """Менеджер заявки"""
    def get_status(self, designer, status):
        return self.get_queryset().filter(designer=designer, status=status)

    def think_today(self, designer):
        now = timezone.now()
        date_now = datetime.date(year=now.year, month=now.month, day=now.day)
        inquery_list = []
        for inquery in self.get_status(designer, self.model.INQUERY_THINK):
            call_back = inquery.get_last_inquery_status().call_back
            if call_back <= date_now:
                inquery_list.append(inquery)
        return inquery_list

    def overdue_think(self, designer):
        now = timezone.now()
        date_now = datetime.date(year=now.year, month=now.month, day=now.day)
        inquery_list = []
        for inquery in self.get_status(designer, self.model.INQUERY_THINK):
            call_back = inquery.get_last_inquery_status().call_back
            try:
                if call_back < date_now:
                    inquery_list.append(inquery)
            except TypeError:
                pass
        return inquery_list

    def overdue_new(self, designer):
        now = timezone.now() - datetime.timedelta(days=1)
        return self.get_status(designer, self.model.INQUERY_NEW).filter(start_datetime__lt=now)


class DesignerManager(models.Manager):
    def all(self):
        return User.objects.filter(user_permissions__codename='is_designer').order_by('first_name', 'last_name')


class BusyManager(models.Manager):
    """Возврашает все события, кроме выходных"""
    def all(self):
        return self.get_queryset().filter(all_day=False)


class InqueryStatusManager(models.Manager):
    def __delete_status(self, status):
        status.hidden = True
        status.inqueryfile_set.all().update(is_delete=True)
        status.save()

        inquery = status.inquery
        prev_status = self.get_prev_status_not_hidden(status.id)
        inquery.status = prev_status.status
        inquery.save()

    def __delete_status_pay(self, status):
        status.hidden = True
        status.inqueryfile_set.all().update(is_delete=True)
        status.save()

        inquery = status.inquery
        prev_status = self.get_prev_status_not_hidden(status.id)
        inquery.status = prev_status.status
        inquery.type_pay = None
        inquery.total_amount = None
        inquery.total_white_goods = None
        inquery.save()

    def delete_status(self, status_id):
        status = self.get_queryset().get(id=int(status_id))
        if status.status == self.model.INQUERY_PAY:
            self.__delete_status_pay(status)
        elif status.status in (self.model.INQUERY_REPEAT, self.model.INQUERY_THINK, self.model.INQUERY_CANCELED,
                               self.model.INQUERY_NOT_PAY):
            self.__delete_status(status)

    def get_prev_status_not_hidden(self, status_id):
        inquery_status = self.get_queryset().get(id=int(status_id))
        inquery = inquery_status.inquery
        prev_status = inquery.inquerystatus_set.filter(hidden=False).order_by('-id')[0]
        return prev_status


class InqueryFileManager(models.Manager):
    def all_not_delete(self):
        return self.get_queryset().filter(is_delete=False)
