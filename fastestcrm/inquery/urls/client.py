from django.urls import re_path

from inquery.views import ClientInclineEditView

urlpatterns = [
    re_path(r'^client/(?P<client_id>\d+)/edit/$', ClientInclineEditView.as_view(), name="edit_client"),
]

