from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
class productsListView(ListView):
    model = Product
    template_name = 'productsList.html'

class productDetailsView(DetailView):
    model = Product
    template_name = 'productDetails.html'

def compareCategories(request):
    template = 'compareProductsForm.html'
    ctx = {
        'form': compareProductsForm(),
        "message": ''
    }

    if request.method == "POST":
        form = compareProductsForm(request.POST)

        if form.is_valid():
            prod1 = form.cleaned_data.get('compare_product1')
            prod2 = form.cleaned_data.get('compare_product2')

            if prod1 == prod2:
                ctx['message'] = 'Non si possono paragonare due prodotti uguali.'
                
            prod1 = Product.objects.get(id=prod1)
            prod2 = Product.objects.get(id=prod2)

            if prod1.category != prod2.category:
                ctx['message'] = 'Non si possono paragonare due prodotti di categorie diverse.'
            
            if ctx['message'] == '':
                return redirect("app_prodotti:compareProducts", prod1.id, prod2.id)
            
    return render(request, template_name=template, context=ctx)

def compareProducts(request, prod1, prod2):
    template = 'compareProducts.html'
    ctx = {
        'prods': [
            Product.objects.get(id=prod1),
            Product.objects.get(id=prod2),
        ]
    }

    return render(request, template_name=template, context=ctx)

class vendorDetailsView(DetailView):
    model = EcommerceUser
    template_name = 'vendorDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id = self.get_object().id
        context['scores'] = VendorScore.objects.filter(id=id)
        nScore = 0
        totalScore = 0
        for score in context['scores']:
            nScore += 1
            totalScore += score.value
        context['totalScore'] = totalScore/nScore

        return context
