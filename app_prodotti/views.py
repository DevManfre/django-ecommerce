from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.
class productsListView(ListView):
    model = Product
    template_name = 'productsList.html'

class productDetailsView(DetailView):
    model = Product
    template_name = 'productDetails.html'