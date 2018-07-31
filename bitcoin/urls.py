from django.conf.urls import include, url
from . import views
from django.contrib import admin
app_name = 'bitcoin'

urlpatterns = [
    url('', views.index, name="index"),
]