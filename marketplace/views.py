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

