from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductMethodTest(TestCase):
    def test_getTotalScore_with_zero_scores(self):
        #Ottenere il punteggio di un prodotto con 0 recensioni
        product = Product(
            name = "Prodotto di Test",
            description= "Test comportamento in assenza di recensioni",
            price = 99.99
        )

        #Mi aspetto 0 come score
        self.assertEqual(product.getTotalScore(), 0)
