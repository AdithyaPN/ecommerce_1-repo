from django.urls import path
from . import views

urlpatterns=[
    path('home', views.customer_home),
    path('cart', views.customer_cart),
    path('product_details', views.customer_productDetails),
    path('my_order', views.customer_myOrder),
    path('customer_changePassword', views.customer_changepassword),
]