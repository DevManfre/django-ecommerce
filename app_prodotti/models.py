from django.db.models import *
from app_utenti.models import EcommerceUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class CategoryBrandCommonInfo(Model):
    STRING_LENGTH = 30

    id = IntegerField(primary_key=True)
    name = CharField(max_length=STRING_LENGTH, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class Category(CategoryBrandCommonInfo):
    class Meta:
        verbose_name_plural = 'Categorie'

class Brand(CategoryBrandCommonInfo):
    class Meta:
        verbose_name_plural = "Brands"

class Product(Model):
    STRING_LENGTH = 100
    MAX_DECIMAL = 2
    MAX_DIGITS = 6
    OTHER_BRAND_ID = OTHER_CATEGORY_ID = DEFAULT_VENDOR = 0

    id = IntegerField(primary_key=True)
    name = CharField(max_length=STRING_LENGTH)
    description = CharField(max_length=STRING_LENGTH*3)
    price = DecimalField(decimal_places=MAX_DECIMAL, max_digits=MAX_DIGITS)
    image = ImageField(default=None)
    category = ForeignKey(Category, on_delete=CASCADE, default=OTHER_CATEGORY_ID)
    brand = ForeignKey(Brand, on_delete=CASCADE, default=OTHER_BRAND_ID)
    vendor = ForeignKey(EcommerceUser, on_delete=CASCADE, default=DEFAULT_VENDOR)

    def __str__(self):
        return f'{self.name}, {self.price}€'
    
    def getScoresInformations(self):
        scores = ProductScore.objects.filter(product=self)
        scoresDetails = []

        for score in scores:
            scoresDetails.append((score))
        
        return scoresDetails

    def getTotalScore(self):
        totalScore = 0
        scores = ProductScore.objects.filter(product=self)
        nScores = len(scores)

        for score in scores:
            totalScore += score.value
        
        try:
            return int(totalScore/nScores)
        except:
            #Non esistono score per questo prodotto
            return 0

    class Meta:
        verbose_name_plural = 'Prodotti'

class CommmonInfoScore(Model):
    MAX_VALUE = 10
    MIN_VALUE = 1
    
    id = IntegerField(primary_key=True)
    value = IntegerField(
        default=5,
        validators=[
            MaxValueValidator(MAX_VALUE),
            MinValueValidator(MIN_VALUE)
        ]
    )
    user = ForeignKey(EcommerceUser, on_delete=CASCADE, null=True)

    def __str__(self):
        return f'{self.id} - {self.user}'

    class Meta:
        abstract = True

class ProductScore(CommmonInfoScore):
    TEXT_LENGTH = 300
    
    product = ForeignKey(Product, on_delete=CASCADE)
    text = CharField(max_length=TEXT_LENGTH, default='')

    class Meta:
        verbose_name_plural = 'Recensioni - Prodotti'

class VendorScore(CommmonInfoScore):
    vendor = ForeignKey(EcommerceUser, on_delete=SET_NULL, null=True, related_name="vendor")

    class Meta:
        verbose_name_plural = 'Recensioni - Venditori'

class Order(Model):
    user = ForeignKey(EcommerceUser, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=CASCADE)
    quantity = IntegerField(default=1)
    date = DateField(default=timezone.now())

    def __str__(self):
        return f'{self.product}'
    
    class Meta:
        verbose_name_plural = 'Ordini'
