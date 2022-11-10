from django.shortcuts import render

# Create your views here.
def index_page(request):
    return render(request, 'commontemplates/index.html')

def seller_login(request):
    return render(request, 'commontemplates/seller_login.html')

def customer_login(request):
    return render(request, 'commontemplates/customer_login.html')    

def seller_signup(request):
    return render(request, 'commontemplates/seller_signup.html')

def customer_signup(request):
    return render(request, 'commontemplates/customer_signup.html')

def change_password(request):
    return render(request, 'commontemplates/change_password.html')

def load_image(request):
    return render(request, 'commontemplates/image.html')

def box_model(request):
    return render(request, 'commontemplates/cssboxmodel.html')

def css_rules(request):
    return render(request, 'commontemplates/cssrules.html')

def demo_box(request):
    return render(request, 'commontemplates/demobox.html')

def cart_view(request):
    return render(request, 'commontemplates/cartview.html')

def grid_demo(request):
    return render(request, 'commontemplates/griddemo.html')

def flex_css(request):
    return render(request, 'commontemplates/flex.html')

def boot_strap(request):
    return render(request, 'commontemplates/bootstrap.html')

def responsive_bootstrap(request):
    return render(request, 'commontemplates/responsive.html')

