from django.urls import path

from .views import DetailFrozeView

urlpatterns = [
    path('', DetailFrozeView, name="calendar_today_url"),
]
