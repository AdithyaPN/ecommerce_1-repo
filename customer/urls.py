from django.urls import path
from . import views

app_name="customer"
urlpatterns=[
    path('home', views.customer_home, name="sellerhome"),
    path('cart', views.customer_cart, name="customercart"),
    path('product_details', views.customer_productDetails),
    path('my_order', views.customer_myOrder, name="myorder"),
    path('customer_changePassword', views.customer_changepassword),
]