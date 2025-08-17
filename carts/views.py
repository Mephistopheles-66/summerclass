from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from Products.models import Product
from .models import Cart, CartItem

# Create your views here.

#private helper: get/create session cart id
def _cart_id(request):
    cart = request.session.session_key

    # If there is no session, create a new session and return the cart id
    if not cart:
        cart = request.session.create()
    return cart    

def add_cart(request, product_id):
    # product = Product.objects.get(id=product_id) #Get product
    product = get_object_or_404(Product, id=product_id)

    try:
        #Get the cart using the cart_id present in the session
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1 # cart_item.quantity = cart_item.quantity + 1
        cart_item.save()
    except CartItem.DoesNotExist:
        
