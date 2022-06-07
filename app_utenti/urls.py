from .views import *
from django.urls import path

app_name = 'app_utenti'

urlpatterns = [
    path('signup/costumer/', costumerSignUp, name='costumerSignUpPage'),
]