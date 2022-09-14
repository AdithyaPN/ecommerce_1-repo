from django.shortcuts import render

# Create your views here.
def customer_home(request):
    return render(request, 'customer_template/home.html')

def customer_cart(request):
    return render(request, 'customer_template/cart.html')

def customer_productDetails(request):
    return render(request, 'customer_template/product_details.html')

def customer_myOrder(request):
    return render(request, 'customer_template/my_order.html')
    
def customer_changepassword(request):
    return render(request, 'customer_template/change_password.html')
