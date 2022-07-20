@register.simple_tag
def count_froze_overdue_new(designer):
    q1 = 'SELECT COUNT(*) FROM (SELECT a.id, a.froze_id, a.call_back, a.start_datetime, a.comment, a.status, a.author_id, a.created_at, a.hidden, b.id FROM'
    q2 = '(SELECT "froze_frozestatus"."id", "froze_frozestatus"."froze_id", "froze_frozestatus"."call_back", "froze_frozestatus"."start_datetime", "froze_frozestatus"."comment", "froze_frozestatus"."status", "froze_frozestatus"."author_id", "froze_frozestatus"."created_at", "froze_frozestatus"."hidden" FROM "froze_frozestatus" WHERE ("froze_frozestatus"."froze_id" IN '
    q3 = '(SELECT U0."id" AS Col1 FROM "froze_froze" U0 WHERE U0."designer_id" = '
    q4 = str(designer.id)
    q5 = ' AND NOT U0."dubl" = true AND (U0."status" = \'new\' OR U0."status" = \'repeat\' OR U0."status" = \'think\')/* AND ko_status = 0*/) '
    q6 = 'AND ("froze_frozestatus"."call_back" < \''
    q7 = now().strftime("%Y-%m-%d")  # '2018-07-31'
    q8 = '\'::date OR "froze_frozestatus"."start_datetime" < \''
    q9 = q7
    q10 = '\'::date))) a INNER JOIN (SELECT DISTINCT ON ("froze_frozestatus"."froze_id") "froze_frozestatus"."id", "froze_frozestatus"."froze_id" FROM "froze_frozestatus" WHERE ('
    q11 = '"froze_frozestatus"."froze_id" IN (SELECT U0."id" AS Col1 FROM "froze_froze" U0 WHERE U0."designer_id" = '
    q12 = q4
    q13 = ' AND NOT U0."dubl" = true AND (U0."status" = \'new\' OR U0."status" = \'repeat\' OR U0."status" = \'think\')/* AND ko_status = 0*/) '
    q14 = ') ORDER BY "froze_frozestatus"."froze_id" DESC, "froze_frozestatus"."id" DESC) b ON (a.id = b.id)) subquery;'
    query = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10 + q11 + q12 + q13 + q14
    return my_custom_sql(query=query)[0][0]