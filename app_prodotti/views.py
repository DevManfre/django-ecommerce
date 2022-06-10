from django.shortcuts import render
from django.views.generic.list import ListView
from .models import *

# Create your views here.
class productsListView(ListView):
    model = Product
    template_name = 'productsList.html'