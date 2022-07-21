from django.db import connection


def my_custom_sql(query):
    """Сырые запросы к БД"""
    with connection.cursor() as cursor:
        cursor.execute(query)
        to_return = cursor.fetchall()
    return to_return
