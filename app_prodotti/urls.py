from .views import *
from django.urls import path

app_name = 'app_prodotti'

urlpatterns = [
    path('productsList/', productsListView.as_view(), name='productsList'),
]