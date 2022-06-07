from django.db.models import *
from django.contrib.auth.models import User

# Create your models here.
class EcommerceUser(User):
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def description(self):
        return f'''
            DATI -> {self}
            EMAIL ->  {self.email}
            PASSWORD -> {self.password}
        '''

    class Meta:
        abstract = True

class Costumer(EcommerceUser):
    class Meta:
        verbose_name_plural = 'Utenti'

class Vendor(EcommerceUser):
    IBAN_LENGTH = 27

    iban = CharField(max_length=IBAN_LENGTH)

    def description(self):
        return super().description() + f"    IBAN -> {self.iban}\n"

    class Meta:
        verbose_name_plural = 'Venditori'
