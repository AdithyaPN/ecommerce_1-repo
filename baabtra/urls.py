from operator import index
from django.urls import path
from . import views


urlpatterns=[
    path('baabtrahome', views.baabtra_home),
    path('javascript', views.java_script),
    path('newjs', views.new_js),
    path('condjs', views.cond_js),
    path('loop', views.loop),
    path('largest', views.largest_among_two),
    path('largestofThree', views.largest_among_three),
    path('sumOfdigits', views.sum_of_digits),
    path('digitReverse', views.digit_reverse),
    path('palindrome', views.palindrome),
    path('greatestdigit', views.greatest_digit),
    path('numberOfdigit', views.numberOf_digit),
    path('hollowsquare', views.hollow_square),
    path('mirror_right_triangle', views.mirror_right_triangle),
    path('pyramid', views.pyramid_star),
    path('inv_pyramid', views.inverted_pyramid),
    path('right_triangle', views.right_triangle),
    path('half_diamond', views.half_diamond),
    path('inv_right_tri', views.inv_right_tri),
    path('do_while', views.do_while),
    path('dom', views.dom),
    path('dom_methods', views.dom_methods),
    path('simple_calculator', views.simple_calculator),
    path('todo', views.to_do),
    path('password', views.password),
    path('jquery', views.jQuery),
    path('addproduct', views.add_product),
    path('viewproduct', views.view_product),
    path('product', views.product),
    path('pTag', views.pjQuery),
    path('webdemo', views.webDemo),
    path('validation', views.validation),
]