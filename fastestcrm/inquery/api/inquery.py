import datetime

from django.utils.timezone import now
from inquery.models import Inquery, InqueryStatus


def get_overdue_inquery_status_new(designer):
    """Получить просроченные запросы со статусом 'Новый'."""
    n = now()
    n = datetime.datetime(n.year, n.month, n.day)
    inquery_items = Inquery.objects \
        .filter(designer=designer, status=Inquery.INQUERY_NEW, inquerystatus__start_datetime__lt=n) \
        .select_related('client') \
        .order_by("inquerystatus__start_datetime")
    return inquery_items


def get_overdue_inquery_status_repeat(designer):
    """Получить просроченные запросы со статусом 'Повторная встреча'."""
    n = datetime.datetime.now()
    n = datetime.datetime(n.year, n.month, n.day)
    inquery_list = []
    for inquery in Inquery.manager.get_status(designer, Inquery.INQUERY_REPEAT):
        start_datetime = inquery.get_last_inquery_status().start_datetime
        if start_datetime is not None and start_datetime < n or start_datetime is None:
            inquery_list.append(inquery)
    return inquery_list
