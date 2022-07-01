from django.forms import *

from app_utenti.models import EcommerceUser

class SignUpForm(Form):
    signup_username = CharField(
        label="",
        max_length=100,
        min_length=3,
        required=True,
        widget=TextInput(attrs={'class': "form-input", 'placeholder': 'Username'})
    )
    signup_first_name = CharField(
        label="",
        max_length=100,
        min_length=3,
        required=True,
        widget=TextInput(attrs={'class': "form-input", 'placeholder': 'Nome'})
    )
    signup_last_name = CharField(
        label="",
        max_length=100,
        min_length=3,
        required=True,
        widget=TextInput(attrs={'class': "form-input", 'placeholder': 'Cognome'})
    )
    signup_email = EmailField(
        label="",
        max_length=254,
        required=True,
        widget=TextInput(attrs={'class': "form-input", 'placeholder': 'Email'})
    )
    signup_password = CharField(
        label='',
        widget=PasswordInput(attrs={'class': "form-input", 'placeholder': 'Password'})
    )
    signup_iban = CharField(
        label="",
        max_length=EcommerceUser.IBAN_LENGTH,
        min_length=EcommerceUser.IBAN_LENGTH,
        required=False,
        widget=TextInput(attrs={'class': "form-input", 'placeholder': 'Iban per essere venditore'})
    )

class LogInForm(Form):
    login_username = CharField(
        label='',
        max_length=254,
        min_length=3,
        required=True,
        widget=TextInput(attrs={'class': "form-input", 'placeholder': 'Username'})
    )
    signup_password = CharField(
        label='',
        widget=PasswordInput(attrs={'class': "form-input", 'placeholder': 'Password'})
    )