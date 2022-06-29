from math import prod
from unicodedata import category
from django.shortcuts import render
from app_prodotti.models import *
from django.db.models import Count

def homepage(request):
    template = "homepage.html"
    ctx = {}

    return render(request, template_name=template, context=ctx)

def welcomePage(request):
    def suggestedProductBySameCategory():
        # Ottengo la categoria più comprata
        mostBoughtCategory_query = f"""
        SELECT app_prodotti_order.id, category_id, COUNT(*) as orderCount
        FROM app_prodotti_order
        INNER JOIN app_prodotti_product ON (app_prodotti_order.product_id = app_prodotti_product.id)
        WHERE user_id='{request.user.id}'
        GROUP BY category_id
        ORDER BY orderCount DESC
        LIMIT 1
        """
        
        mostBoughtCategory = Category.objects.get(id=Order.objects.raw(mostBoughtCategory_query)[0].category_id).id

        #Ottengo i prodotti di quella categoria comprati dall'utente
        mostBoughtCategoryBoughtProducts_query = f"""
        SELECT app_prodotti_product.id
        FROM app_prodotti_order
        INNER JOIN app_prodotti_product ON (app_prodotti_order.product_id = app_prodotti_product.id)
        WHERE user_id='{request.user.id}' AND category_id='{mostBoughtCategory}'
        """

        mostBoughtCategoryProducts = [product.id for product in Product.objects.raw(mostBoughtCategoryBoughtProducts_query)]

        #Creo la lista di prodotti della stessa categoria ed escludo quelli comprati 
        products = Product.objects.filter(category_id=mostBoughtCategory)

        for boughtProduct in mostBoughtCategoryProducts:
            products = products.exclude(id=boughtProduct)

        if len(products)>5:
            return products[0,5]
        
        return products
    
    def suggestedProductBySameBrand():
        #Ottengo il brand più comprato
        mostBoughtBrand_query = f"""
        SELECT app_prodotti_order.id, brand_id, COUNT(*) as orderCount
        FROM app_prodotti_order
        INNER JOIN app_prodotti_product ON (app_prodotti_order.product_id = app_prodotti_product.id)
        WHERE user_id='{request.user.id}'
        GROUP BY brand_id
        ORDER BY orderCount DESC
        LIMIT 1
        """

        mostBoughtBrand = Category.objects.get(id=Brand.objects.raw(mostBoughtBrand_query)[0].brand_id).id

        #Ottengo i prodotti di quel brand comprati dall'utente
        mostBoughtBrandBoughtProducts_query = f"""
        SELECT app_prodotti_product.id
        FROM app_prodotti_order
        INNER JOIN app_prodotti_product ON (app_prodotti_order.product_id = app_prodotti_product.id)
        WHERE user_id='{request.user.id}' AND brand_id='{mostBoughtBrand}'
        """

        mostBoughtBrandProducts = [product.id for product in Product.objects.raw(mostBoughtBrandBoughtProducts_query)]

        #Creo la lista di prodotti dello stesso brand ed escludo quelli comprati 
        products = Product.objects.filter(brand_id=mostBoughtBrand)

        for boughtProduct in mostBoughtBrandProducts:
            products = products.exclude(id=boughtProduct)

        if len(products)>5:
            return products[0,5]
        
        return products

    template = "welcomePage.html"
    ctx = {}

    if request.user.is_authenticated:
        # Recommendation System
        ctx['suggestedProductBySameCategory'] = suggestedProductBySameCategory()
        ctx['suggestedProductBySameBrand'] = suggestedProductBySameBrand()

    return render(request, template_name=template, context=ctx)

def vendorWelcomePage(request):
    template = "vendorWelcomePage.html"
    ctx = {}

    return render(request, template_name=template, context=ctx)
