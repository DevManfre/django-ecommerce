"""sito_ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from .views import *
from .initDbCmds import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    re_path(r'^$|^/$|^home/$|^homepage/$', homepage, name='homepage'),
    
    path('login/user/', welcomePage, name="welcomePage"),
    path('login/vendor/', vendorWelcomePage, name="vendorWelcomePage"),

    path('user/', include('app_utenti.urls')),
    path ('product/', include('app_prodotti.urls')),
]

# CODICE DA ESEGUIRE ALL'AVVIO DI DJANGO
eraseDatabase()
initDatabase() 