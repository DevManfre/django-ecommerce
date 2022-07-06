from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils import timezone
import shutil
import os
from pathlib import Path

# Create your views here.
class productsListView(ListView):
    model = Product
    template_name = 'productsList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['object_list'] = context['object_list'].order_by('name')

        return context 

class myProductsListView(ListView):
    model = Product
    template_name = 'myProductsList.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        source_dir = Path(__file__).resolve().parent.parent
        dest_dir = Path(__file__).resolve().parent.parent
        dest_dir = os.path.join(dest_dir, 'static')

        print(dest_dir)
        dirFiles = os.listdir(source_dir)
        dirFiles.remove('.git')
        dirFiles.remove('.gitignore')
        dirFiles.remove('app_prodotti')
        dirFiles.remove('app_utenti')
        dirFiles.remove('db.sqlite3')
        dirFiles.remove('LICENSE')
        dirFiles.remove('manage.py')
        dirFiles.remove('Pipfile')
        dirFiles.remove('Pipfile.lock')
        dirFiles.remove('README.md')
        dirFiles.remove('sito_ecommerce')
        dirFiles.remove('static')
        dirFiles.remove('templates')
        
        for img in dirFiles:
            shutil.move(f"{source_dir}/{img}", f"{dest_dir}/{img}")

        context['object_list'] = Product.objects.filter(vendor_id=self.request.user.id)

        return context 

class productDetailsView(DetailView):
    model = Product
    template_name = 'productDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['isReviewed'] = False

        try:
            if self.request.user.is_authenticated:
                productId = self.get_object().id
                userId = User.objects.get(username=self.request.user).id
                review = ProductScore.objects.get(product_id=productId, user_id=userId)


                if review:
                    context['isReviewed'] = True
        except:
            pass

        return context

def compareCategories(request):
    template = 'compareProductsForm.html'
    ctx = {
        'form': compareProductsForm(),
        "message": '',
        'error': False
    }

    if request.method == "POST":
        form = compareProductsForm(request.POST)

        if form.is_valid():
            prod1 = form.cleaned_data.get('compare_product1')
            prod2 = form.cleaned_data.get('compare_product2')

            if prod1 == prod2:
                ctx['error'] = True
                ctx['message'] = 'Non si possono paragonare due prodotti uguali'
                
            prod1 = Product.objects.get(id=prod1)
            prod2 = Product.objects.get(id=prod2)

            if prod1.category != prod2.category:
                ctx['error'] = True
                ctx['message'] = 'Non si possono paragonare due prodotti di categorie diverse'
            
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
        
        context['isReviewed'] = False
        context['vendorId'] = self.get_object().id
        id = self.get_object().id
        nScore = 0
        totalScore = 0

        for score in VendorScore.objects.filter(vendor_id=id):
            nScore += 1
            totalScore += score.value
        try:
            context['totalScore'] = int(totalScore/nScore)
        except:
            context['totalScore'] = 0

        try:
            if self.request.user.is_authenticated:
                vendorId = self.get_object().id
                userId = User.objects.get(username=self.request.user).id
                review = VendorScore.objects.filter(vendor_id=vendorId, user_id=userId)

                if len(review) > 0:
                    context['isReviewed'] = True
        except:
            pass

        return context 

def vendorReview(request, pk):
    template = 'reviewForm.html'
    ctx = {
        'form': vendorReviewForm(),
        "message": '',
        "vendor": pk
    }

    if request.method == "POST":
        form = vendorReviewForm(request.POST)

        if form.is_valid():
            score = VendorScore()
            score.value = form.cleaned_data.get('review_value')
            score.user = EcommerceUser.objects.get(username=request.user.username)
            score.vendor = EcommerceUser.objects.get(id=pk)

            score.save()

            return redirect("app_prodotti:vendorDetails", pk)

    return render(request, template_name=template, context=ctx)

def productReview(request, pk):
    template = 'reviewForm.html'
    ctx = {
        'form': productReviewForm(),
        "message": '',
        "vendor": None,
        "product": pk
    }

    if request.method == "POST":
        form = productReviewForm(request.POST)

        if form.is_valid():
            score = ProductScore()
            score.value = form.cleaned_data.get('review_value')
            score.product = Product.objects.get(id=pk)
            score.user = EcommerceUser.objects.get(username=request.user.username)
            
            score.save()

            return redirect("app_prodotti:productDetails", pk)

    return render(request, template_name=template, context=ctx)

def productStats(request, pk):
    template = 'productStats.html'
    ctx = {
        'object': Product.objects.get(id=pk)
    }

    orders = Order.objects.filter(product_id=pk, order_type=2)
    totalItems = 0

    ctx['totalOrders'] = len(orders)

    for order in orders:
        totalItems += order.quantity
    
    ctx['totalItems'] = totalItems
    ctx['totalGain'] = totalItems*ctx['object'].price

    return render(request, template_name=template, context=ctx)

def deleteProduct(request, pk):
    Product.objects.get(id=pk).delete()

    return redirect('app_prodotti:myProductsList')

class createProduct(CreateView):
    model = Product
    template_name = "createProduct.html"
    fields = [
        'name',
        'description',
        'price',
        'category',
        'brand',
        'image'
    ]
    success_url = reverse_lazy("app_prodotti:myProductsList")

    def form_valid(self, form):
        form.instance.vendor_id = self.request.user.id

        return super().form_valid(form)

def searchResults(request):
    template = 'searchResults.html'
    ctx = {
        "searched": False,
        "categories": Category.objects.all(),
        "maxPrice": Product.objects.first().price
    }

    for product in Product.objects.all():
        if ctx['maxPrice'] < product.price:
            ctx['maxPrice'] = int(product.price)
    
    ctx['minValue'] = int(ctx['maxPrice']/4)
    ctx['maxValue'] = int(ctx['maxPrice']/4*3)

    if request.method == "POST":
        ctx['searched'] = True
        ctx['searchedText'] = request.POST['text']
        ctx['items'] = Product.objects.filter(name__contains=request.POST['text']).order_by('name')
        
        if request.POST['category'] != 'All':
            ctx['items'] = ctx['items'].filter(category_id=Category.objects.get(name=request.POST['category']).id)

        ctx['items'] = ctx['items'].filter(price__range=(request.POST['minPrice'], request.POST['maxPrice']))
    
    return render(request, template_name=template, context=ctx)

def chronology(request):
    template = 'chronology.html'
    ctx = {
        'orders': Order.objects.filter(user_id=request.user.id, order_type=3).order_by('-date').select_related('product')
    }
    
    return render(request, template_name=template, context=ctx)

def addToCart(request, pk):
    try:
        quantity = int(request.POST['quantity'])
    except:
        return redirect('app_prodotti:productDetails', pk)

    if quantity > 0:
        order = Order(
            user = EcommerceUser.objects.get(id=request.user.id),
            product = Product.objects.get(id=pk),
            quantity = quantity,
            date = timezone.now(),
            order_type = 0
        )

        order.save()

    return redirect('app_prodotti:productDetails', pk)

def cart(request):
    template = 'cart.html'
    ctx = {
        'orders': Order.objects.filter(user_id=request.user.id, order_type=0)
    }

    
    return render(request, template_name=template, context=ctx)

def cartPay(request, pk):
    template = 'cartPay.html'
    ctx = {
        'orders': Order.objects.filter(user_id=request.user.id, order_type=0),
        'totalPrice': 0,
        'iban': '', 
        'buy_all': False,
        'lst': []
    }

    if pk == -1:
        order = Order.objects.get(id=pk)
        order.order_type = 1
        order.save()

        ctx['totalPrice'] = order.product.price * order.quantity
        ctx['iban'] = order.product.vendor.iban
    else:
        ctx['buy_all'] = True

        for order in ctx['orders']:
            """ order.order_type = 1
            order.save() """

            order.total = order.product.price * order.quantity

    return render(request, template_name=template, context=ctx)