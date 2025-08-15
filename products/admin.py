from django.contrib import admin
from .models import Category, Product
from django.utils.html import format_html

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}
      



class ProductAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('name', 'category', 'price', 'stock', 'status', 'image_preview')
    search_fields =("name",)
    list_filter = ("category",)
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('image_preview',)   

    def image_preview(self, obj):
        if obj.product_image:
            return format_html('<img src="{}" width="80" style="object-fit:cover;" />', obj.product_image.url)
        return "No image"
    image_preview.short_description = 'Image'    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
