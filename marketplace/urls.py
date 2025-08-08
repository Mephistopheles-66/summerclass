"""
URL configuration for marketplace project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', include('products.urls')),
    path('blogs/', include('blog.urls')),
    path('pages/', include('pages.urls')),
    #cart
    path('cart/', views.cart, name="cart"),
    #orders
    path('checkout/', views.checkout, name="checkout"),
    path('my-orders/', views.my_orders, name="my_orders"),
    path('order-complete/', views.order_complete, name="order_complete"),
    path('place-order/', views.place_order, name="place_order"),
    #user
    path('dashboard/', views.user_dashboard, name="user_dashboard"),
    path('login/', views.user_login, name="login"),
    path('register/', views.user_register, name="register"),
    path('change-password/', views.user_changepassword, name="change_password"),
    path('edit-profile/', views.user_edit_profile, name="change_password"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
