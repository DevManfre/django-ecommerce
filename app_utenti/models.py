from django.db.models import *
from django.contrib.auth.models import User

# Create your models here.
class EcommerceUser(User):
    IBAN_LENGTH = 27

    iban = CharField(max_length=IBAN_LENGTH)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def description(self):
        return f'''
            DATI -> {self}
            EMAIL ->  {self.email}
            PASSWORD -> {self.password}
            IBAN -> {self.iban}
        '''

