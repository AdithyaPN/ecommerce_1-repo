from django.urls import path
from . import views

urlpatterns=[
    path('admin_login', views.admin_login),
    path('admin_home', views.admin_home),
    path('approveSeller', views.admin_approveSeller),
    path('viewCustomer', views.admin_viewCustomer),
    path('viewSeller', views.admin_viewSeller),
    path('viewSellerorders', views.admin_viewSellerorders),
]