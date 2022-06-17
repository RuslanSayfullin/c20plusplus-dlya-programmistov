from django.urls import re_path

from inquery.views import NewInqueryView


urlpatterns = [
    re_path(r'^froze/new/$', NewInqueryView.as_view(), name="new_froze_url"),     # Контроллер для нового новой заявки
]