from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
from blog.models import blog, blogcategory
from django.apps import AppConfig



def home(request):
    products = Product.objects.all()
    blogs = blog.objects.all()
    return render(request, 'home/home1.html', {
        'products': products,
        'blogs': blogs

        })

def user_login(request):
    return render(request, "user/login.html")


def user_register(request):
    return render(request, "user/register.html")

def user_dashboard(request):
    return render(request, "user/dashboard.html")

def user_edit_profile(request):
    return render(request, "user/edit_profile.html")

def cart(request):
    return render(request, "cart/cart.html")

def user_changepassword(request):
    return render(request, "user/change_password.html")

def checkout(request):
    return render(request, "orders/checkout.html")

def my_orders(request):
    return render(request, "orders/my_orders.html")

def order_complete(request):
    return render(request, "orders/order_complete.html")

def place_order(request):
    return render(request, "orders/place_order.html")
