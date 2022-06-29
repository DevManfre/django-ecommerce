from .views import *
from django.urls import path

app_name = 'app_utenti'

urlpatterns = [
    path('signup/', signupPage, name='signupPage'),
    path('login/', loginPage, name='loginPage')
]