from django.forms import *

class SignUpFormCostumer(Form):
    signup_username = CharField(label="Username", max_length=100, min_length=3, required=True)
    signup_first_name = CharField(label="Nome", max_length=100, min_length=3, required=True)
    signup_last_name = CharField(label="Cognome", max_length=100, min_length=3, required=True)
    signup_email = EmailField(label="Email", max_length=254, required=True)
    signup_password = CharField(label='Password', widget=PasswordInput())
