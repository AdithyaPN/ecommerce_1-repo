from django.shortcuts import render

# Create your views here.
def seller_home(request):
    return render(request, 'sellertemplates/sellerhome.html')

def seller_cart(request):
    return render(request, 'sellertemplates/sellerCart.html')


def seller_myOrders(request):
    return render(request, 'sellertemplates/my_orders.html')

def seller_addProduct(request):
    return render(request, 'sellertemplates/addProduct.html')

def seller_changePassword(request):
    return render(request, 'sellertemplates/seller_changepassword.html')
    
def seller_updateStock(request):
    return render(request, 'sellertemplates/update_stock.html')