from .views import *
from django.urls import path

app_name = 'app_prodotti'

urlpatterns = [
    path('productsList/', productsListView.as_view(), name='productsList'),
    path('productDetails/<pk>/', productDetailsView.as_view(), name='productDetails'),
    path('compare/categories/', compareCategories, name='compareCategories'),
    path('compare/products/<int:prod1>/<int:prod2>/', compareProducts, name='compareProducts'),
    path('vendorDetails/<pk>/', vendorDetailsView.as_view(), name='vendorDetails'),
    path('vendorReview/<pk>/', vendorReview, name='vendorReview'),
    path('productReview/<pk>/', productReview, name='productReview'),
    path('productsList/vendor/', myProductsListView.as_view(), name='myProductsList'),
    path('productStats/<pk>/', productStats, name='productStats'),
    path('deleteProduct/<pk>/', deleteProduct, name='deleteProduct'),
    path('createProduct/', createProduct.as_view(), name='createProduct'),
    path('searchResults/', searchResults, name="searchResults"),
    path('chronology/', chronology, name="chronology")
]