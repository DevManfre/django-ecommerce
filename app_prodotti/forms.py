from django.forms import *
from .models import *

class compareProductsForm(Form):
    CHOICE_LIST = [(f'{i.id}', f'{i}') for i in Product.objects.all()]

    compare_product1 = ChoiceField(label="Primo Prodotto ", required=True,choices=CHOICE_LIST)
    compare_product2 = ChoiceField(label="Secondo Prodotto ", required=True,choices=CHOICE_LIST)