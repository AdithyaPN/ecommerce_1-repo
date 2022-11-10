from django.shortcuts import render

# Create your views here.
def baabtra_home(request):
    return render(request, 'baabtratemplates/baabtrahome.html')

def java_script(request):
    return render(request, 'baabtratemplates/javascript.html')

def new_js(request):
    return render(request, 'baabtratemplates/newjs.html')

def cond_js(request):
    return render(request, 'baabtratemplates/conditional.html')

def loop(request):
    return render(request, 'baabtratemplates/loop.html')

def largest_among_two(request):
    return render(request, 'baabtratemplates/largest_among_two.html')

def largest_among_three(request):
    return render(request, 'baabtratemplates/largest_among_three.html')

def sum_of_digits(request):
    return render(request, 'baabtratemplates/sumofdigits.html')

def digit_reverse(request):
    return render(request, 'baabtratemplates/digitReverse.html')

def palindrome(request):
    return render(request, 'baabtratemplates/palindrome.html')

def greatest_digit(request):
    return render(request, 'baabtratemplates/greatestdigit.html')

def numberOf_digit(request):
    return render(request, 'baabtratemplates/numberofdigits.html')

def hollow_square(request):
    return render(request, 'baabtratemplates/hollowsquare.html')

def mirror_right_triangle(request):
    return render(request, 'baabtratemplates/mirror_righttriangle.html')

def pyramid_star(request):
    return render(request, 'baabtratemplates/pyramid.html')

def inverted_pyramid(request):
    return render(request, 'baabtratemplates/inverted_pyramid.html')

def right_triangle(request):
    return render(request, 'baabtratemplates/right_triangle.html')

def half_diamond(request):
    return render(request, 'baabtratemplates/halfdiamond.html')

def inv_right_tri(request):
    return render(request, 'baabtratemplates/inverted_right_triangle.html')

def do_while(request):
    return render(request, 'baabtratemplates/do_while.html')

def dom(request):
    return render(request, 'baabtratemplates/dom.html')

def dom_methods(request):
    return render(request, 'baabtratemplates/dom_methods.html')

def simple_calculator(request):
    return render(request, 'baabtratemplates/simple_calculator.html')

def to_do(request):
    return render(request, 'baabtratemplates/todo.html')

def password(request):
    return render(request, 'baabtratemplates/password.html')

def jQuery(request):
    return render(request, 'baabtratemplates/jquery.html')

def product(request):
    return render(request, 'baabtratemplates/product.html')

def add_product(request):
    return render(request, 'baabtratemplates/addproduct.html')

def view_product(request):
    return render(request, 'baabtratemplates/viewproduct.html')

def pjQuery(request):
    return render(request, 'baabtratemplates/jquryPtag.html')

def webDemo(request):
    return render(request, 'baabtratemplates/webdemo.html')

def validation(request):
    return render(request, 'baabtratemplates/validation.html')
