from .client import urlpatterns as client_urlpatterns
from .inquery import urlpatterns as inquery_urlpatterns

urlpatterns = client_urlpatterns + \
    inquery_urlpatterns

