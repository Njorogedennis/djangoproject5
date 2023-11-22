from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views import View

from .forms import CreateUserForm, ProductForm
from django.shortcuts import render, redirect
from .models import CartItem, Product, Cart


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form': form}
    return render(request, 'registration/register.html', context)

def loginpage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('productlist')
            else:
                messages.error(request, 'Invalid username or password. Please try again.')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'registration/login.html', context)

def school(request):
    # Your view logic for the root URL goes here
    return render(request, 'registration/login.html')  # Adjust the template name as needed

def index_view(request):
    return render(request, 'soko fresh/index.html')

def index_view_2(request):
    return render(request, 'soko fresh/index_2.html')

def about_view(request):
    return render(request, 'soko fresh/about.html')

def cart_view(request):
    return render(request, 'soko fresh/cart.html')

def checkout_view(request):
    return render(request, 'soko fresh/checkout.html')

def contact_view(request):
    return render(request, 'soko fresh/contact.html')

def news_view(request):
    return render(request, 'soko fresh/news.html')

def product_view(request):
    return render(request, 'soko fresh/product form.html')

def shop_view(request):
    return render(request, 'soko fresh/shop.html')

def single_news_view(request):
    return render(request, 'soko fresh/single-news.html')

def single_product_view(request):
    return render(request, 'soko fresh/single-product.html')


# views.py




class ProductsView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'soko fresh/index.html', {'products': products})

class AddToCartView(View):
    def get(self, request, product_id):
        product = Product.objects.get(pk=product_id)

        # Get or create a cart for the current user (assuming you have user authentication)
        cart, created = Cart.objects.get_or_create()

        # Add the product to the cart
        cart.products.add(product)

        return redirect('cart_view')

class CartView(View):
    def get(self, request):
        # Get or create a cart for the current user
        cart, created = Cart.objects.get_or_create()

        return render(request, 'soko fresh/cart.html', {'cart': cart})
