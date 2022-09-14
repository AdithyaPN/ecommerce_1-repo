from django.urls import path
from . import views


urlpatterns=[
    path('sellerhome', views.seller_home),
    path('sellerCart', views.seller_cart),
    path('sellerMyorders', views.seller_myOrders),
    path('addProduct', views.seller_addProduct),
    path('changePassword', views.seller_changePassword),
    path('updateStock', views.seller_updateStock),
]