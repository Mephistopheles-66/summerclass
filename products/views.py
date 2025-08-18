from django.shortcuts import render, get_object_or_404
from . models import Category, Product
from django.http import Http404
from carts.models import CartItem
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.


def products(request, category_slug=None):
    categories = None
    products = None

    #Using slug to find the category, if found filter according to the slug

    if category_slug != None:
      categories = get_object_or_404(Category, slug = category_slug)
      products = Product.objects. filter(category=categories, status=True)
      paginator = Paginator (products, 3) #6 is the number of products to display
      page = request.GET.get ('page') #Capturing the page from the link /store/?page=2
      paged_products = paginator.get_page(page)
      product_count = len(paged_products)
    
    else:

    # Fetch all products where status is true and order by id
      products = Product.objects.all().filter(status=True).order_by( 'id')
      paginator = Paginator (products, 3) #6 is the number of products to display
      page = request.GET.get( 'page') #Capturing the page from the link /store/?pager2
      paged_products = paginator.get_page (page)
      product_count = len(paged_products)

    context = {
      'products': paged_products,
      'product_count' : product_count,
    }  
    
    return render(request, 'products/products1.html', context)

def product_detail(request, category_slug, product_slug):
  try:  
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product).exists()
  except Product.DoesNotExist:
    raise Http404("Product Not Found")
  
  context = {
     'product' : product,
     'in_cart' : in_cart
  }
  return render(request, 'products/details1.html', context)

def search(request):
  if 'keyword' in request.GET:
    keyword = request. GET.get('keyword', '').strip()
    products = Product. objects. none()
  if keyword:
    # Search in multiple fields: description or product_name
    products = Product.objects.order_by('-created_date').filter(
      Q(description_icontains=keyword) | Q (product_name_icontains=keyword)

  )
  context = {
    'products': products,
    'product_count': products. count ()
  }
  return render(request, 'products/products.html', context)