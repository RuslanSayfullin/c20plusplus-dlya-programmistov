from django import template
from django.utils.timezone import now

from inquery.templatetags.custom_sql import my_custom_sql

register = template.Library()


@register.simple_tag
def count_inquery_overdue(designer):
    """Вернуть количество просроченных запросов."""
    return count_inquery_overdue_new(designer=designer)
    l = []
    for a in chain(api.inquery.get_overdue_inquery_status_new(designer), api.inquery.get_overdue_inquery_status_repeat(designer), Inquery.manager.overdue_think(designer)):
        if a.ko_status != 0 or a.dubl:
            continue
        l.append(a)
    return len(l)
    inquery_items = (len(api.inquery.get_inquery_inquery_status_new(designer)),
                   len(api.inquery.get_overdue_inquery_status_repeat(designer)),
                   len(Inquery.manager.overdue_think(designer)))
    return sum(inquery_items)


@register.simple_tag
def count_inquery_overdue_new(designer):
    """количество просроченных запросов со статусом 'Новый'."""
    q1 = 'SELECT COUNT(*) FROM (SELECT a.id, a.inquery_id, a.call_back, a.start_datetime, a.comment, a.status, a.author_id, a.created_at, a.hidden, b.id FROM'
    q2 = '(SELECT "inquery_inquerystatus"."id", "inquery_inquerystatus"."inquery_id", "inquery_inquerystatus"."call_back", "inquery_inquerystatus"."start_datetime", "inquery_inquerystatus"."comment", "inquery_inquerystatus"."status", "inquery_inquerystatus"."author_id", "inquery_inquerystatus"."created_at", "inquery_inquerystatus"."hidden" FROM "inquery_inquerystatus" WHERE ("inquery_inquerystatus"."inquery_id" IN '
    q3 = '(SELECT U0."id" AS Col1 FROM "inquery_inquery" U0 WHERE U0."designer_id" = '
    q4 = str(designer.id)
    q5 = ' AND NOT U0."dubl" = true AND (U0."status" = \'new\' OR U0."status" = \'repeat\' OR U0."status" = \'think\')/* AND ko_status = 0*/) '
    q6 = 'AND ("inquery_inquerystatus"."call_back" < \''
    q7 = now().strftime("%Y-%m-%d")  
    q8 = '\'::date OR "inquery_inquerystatus"."start_datetime" < \''
    q9 = q7
    q10 = '\'::date))) a INNER JOIN (SELECT DISTINCT ON ("inquery_inquerystatus"."inquery_id") "inquery_inquerystatus"."id", "inquery_inquerystatus"."inquery_id" FROM "inquery_inquerystatus" WHERE ('
    q11 = '"inquery_inquerystatus"."inquery_id" IN (SELECT U0."id" AS Col1 FROM "inquery_inquery" U0 WHERE U0."designer_id" = '
    q12 = q4
    q13 = ' AND NOT U0."dubl" = true AND (U0."status" = \'new\' OR U0."status" = \'repeat\' OR U0."status" = \'think\')/* AND ko_status = 0*/) '
    q14 = ') ORDER BY "inquery_inquerystatus"."inquery_id" DESC, "inquery_inquerystatus"."id" DESC) b ON (a.id = b.id)) subquery;'
    query = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10 + q11 + q12 + q13 + q14
    return my_custom_sql(query=query)[0][0]


@register.simple_tag
def count_inquery_today(designer):
    """Возвращает количество заявок на сегодня"""
    return count_inquery_today_new(designer=designer)
    _now = now()

    inquery_items = Inquery.objects \
        .filter(designer=designer,
                inquerystatus__start_datetime__year=_now.year,
                inquerystatus__start_datetime__month=_now.month,
                inquerystatus__start_datetime__day=_now.day
                ) \
        .filter(Q(status=Inquery.INQUERY_NEW) | Q(status=Inquery.INQUERY_REPEAT)) \
        .exclude(dubl=True) \
        .select_related('client') \
        .order_by("inquerystatus__start_datetime")

    date_now = datetime.date(year=now().year, month=now().month, day=now().day)
    inquery_list = []
    for inquery in inquery_.manager.get_status(designer, Inquery.INQUERY_THINK):
        call_back = inquery.get_last_inquery_status().call_back
        if call_back == date_now:
            inquery_list.append(inquery)
    the_len = 0
    for a in chain(inquery_items, inquery_list):
        the_len += 1
    return the_len


@register.simple_tag
def count_inquery_today_new(designer):
    """количество заявок на сегодня со статусом 'Новый'."""
    q1 = 'SELECT COUNT(*) FROM (SELECT  a.id, a.inquery_id, a.call_back, a.start_datetime, a.comment, a.status, a.author_id, a.created_at, b.id FROM (SELECT "inquery_inquerystatus"."id", "inquery_inquerystatus"."inquery_id", "inquery_inquerystatus"."call_back", "inquery_inquerystatus"."start_datetime", "inquery_inquerystatus"."comment", "inquery_inquerystatus"."status", "inquery_inquerystatus"."author_id", "inquery_inquerystatus"."created_at", "inquery_inquerystatus"."hidden" FROM "inquery_inquerystatus" '
    q2 = 'WHERE "inquery_inquerystatus"."inquery_id" IN (SELECT U0."id" AS Col1 FROM "inquery_inquery" U0 WHERE (U0."designer_id" = '
    q3 = str(designer.id)
    q4 = ' AND NOT (U0."dubl" = true AND U0."dubl" IS NOT NULL))) AND ("inquery_inquerystatus"."call_back" = \''
    q5 = now().strftime("%Y-%m-%d")
    q6 = '\'::date OR "inquery_inquerystatus"."start_datetime"::date = date \''
    q7 = q5
    q8 = '\')) a INNER JOIN (SELECT DISTINCT ON ("inquery_inquerystatus"."inquery_id") "inquery_inquerystatus"."id", "inquery_inquerystatus"."inquery_id", "inquery_inquerystatus"."call_back", "inquery_inquerystatus"."start_datetime", "inquery_inquerystatus"."comment", "inquery_inquerystatus"."status", "inquery_inquerystatus"."author_id", "inquery_inquerystatus"."created_at", "inquery_inquerystatus"."hidden" FROM "inquery_inquerystatus" WHERE ("inquery_inquerystatus"."inquery_id" IN (SELECT U0."id" AS Col1 FROM "inquery_inquery" U0 WHERE (U0."designer_id" = '
    q9 = q3
    q10 = ' AND NOT (U0."dubl" = true AND U0."dubl" IS NOT NULL)))) ORDER BY "inquery_inquerystatus"."inquery_id" DESC, "inquery_inquerystatus"."id" DESC) b ON (a.id = b.id)) subquery;'
    query = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
    # args=('think', 2, True, datetime.date(2018, 7, 31))
    return my_custom_sql(query=query)[0][0]
