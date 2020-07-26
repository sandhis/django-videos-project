from django.conf.urls import url
from .views import (
    login_view,
)

urlpatterns = [
    url(r"^login/$", login_view, name = "login"),
]