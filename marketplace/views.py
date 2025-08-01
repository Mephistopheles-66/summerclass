from django.shortcuts import render
from django.http import HttpResponse
from products.models import Category, Product
from blog.models import blog, blogcategory



def home(request):
    product = Product.objects.all()
    blogs = blog.objects.all()
    return render(request, 'home/home1.html', {
        'products': product,
        'blogs': blogs
        })

