from django.urls import path
from dashboard.views import Dashboard
from django.conf.urls import url

urlpatterns = [
    path('', Dashboard.as_view(), name='index'),
]
