from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include, url
from .views import (
    home_view,
    AddForm,
)

urlpatterns = [
    url(r'^AddForm/$', AddForm, name='AddForm'),
    url(r'^home_view/$', home_view, name='home_view'),
]
