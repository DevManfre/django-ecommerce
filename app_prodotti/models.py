from ast import Mod
from email.policy import default
from django.db.models import *

# Create your models here.
class CommonInfo(Model):
    STRING_LENGTH = 30

    id = IntegerField(primary_key=True)
    name = CharField(max_length=STRING_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Category(CommonInfo):
    class Meta:
        verbose_name_plural = 'Categorie'

class Brand(CommonInfo):
    class Meta:
        verbose_name_plural = "Brands"

class Product(Model):
    STRING_LENGTH = 100
    MAX_DECIMAL = 2
    MAX_DIGITS = 6
    OTHER_BRAND_ID = OTHER_CATEGORY_ID = 0

    name = CharField(max_length=STRING_LENGTH)
    description = CharField(max_length=STRING_LENGTH*3)
    price = DecimalField(decimal_places=MAX_DECIMAL, max_digits=MAX_DIGITS)
    image = ImageField(default=None)
    category = ForeignKey(Category, on_delete=CASCADE, default=OTHER_CATEGORY_ID)
    brand = ForeignKey(Brand, on_delete=CASCADE, default=OTHER_BRAND_ID)

    def __str__(self):
        return f'{self.name}, {self.price}€'

    class Meta:
        verbose_name_plural = 'Prodotti'

