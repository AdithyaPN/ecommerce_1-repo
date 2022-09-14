from django.shortcuts import render

# Create your views here.
def admin_login(request):
    return render(request, 'ecomadmintemplates/admin_login.html')

def admin_home(request):
    return render(request, 'ecomadmintemplates/admin_home.html')

def admin_approveSeller(request):
    return render(request, 'ecomadmintemplates/approve_seller.html')

def admin_viewCustomer(request):
    return render(request, 'ecomadmintemplates/view_customer.html')

def admin_viewSeller(request):
    return render(request, 'ecomadmintemplates/view_seller.html')

def admin_viewSellerorders(request):
    return render(request, 'ecomadmintemplates/view_sellerOrders.html')
