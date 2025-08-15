from django.shortcuts import render, get_object_or_404
from . models import Category, Product
from django.http import Http404

# Create your views here.

def products(request):
    all_products = Product.objects.all()
    return render(request, 'products/products1.html', {'products': all_products})

def product_detail(request, category_slug, product_slug):
  try:  
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    #in_cart = Cartitem.objects.filter(cart__cart_id=cart_id(request), product=product).exists()
  except Product.DoesNotExist:
    raise Http404("Product Not Found")
  
  context = {
     'product' : product,
     #'in_cart' : incart
  }
  return render(request, 'products/details1.html', context)