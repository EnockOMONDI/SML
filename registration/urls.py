from django.urls import re_path, include
from . import views

app_name = "registration"

urlpatterns = [
    re_path(r'^register_modal$', views.register_modal),
    re_path(r'^register$', views.register),
    re_path(r'^redirected-register$', views.redirectedregister),
]
