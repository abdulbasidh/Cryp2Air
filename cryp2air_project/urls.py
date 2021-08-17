"""cryp2air_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from form.views import RegistrationAction, registration, DashboardView, login, LoginAction, registrationError, setcookie, getcookie, delcookie, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^RegistrationAction/$', RegistrationAction, name='RegistrationAction'),
    url(r'^registrationError/$', registrationError, name='registrationError'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^LoginAction/$', LoginAction, name='LoginAction'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='Logout'),
    path('dashboard/', DashboardView, name="Dashboard"),
    path('scookie',setcookie),
    path('gcookie',getcookie),
    path('dcookie',delcookie)
]
