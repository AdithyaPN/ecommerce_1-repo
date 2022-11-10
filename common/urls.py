from operator import index
from django.urls import path
from . import views


urlpatterns=[
    path('', views.index_page),
    path('seller_login', views.seller_login),
    path('customer_login', views.customer_login),
    path('seller_signup', views.seller_signup),
    path('customer_signup', views.customer_signup),
    path('change_password', views.change_password),
    path('image', views.load_image),
    path('boxmodel', views.box_model),
    path('cssrules', views.css_rules),
    path('demobox', views.demo_box),
    path('cartview', views.cart_view),
    path('griddemo', views.grid_demo),
    path('flex', views.flex_css),
    path('responsive', views.responsive_bootstrap),

]