from django.contrib import admin
from . models import blogcategory, blog

class blogcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class blogAdmin(admin.ModelAdmin):
    exclude = ('created_at',)
    list_display = ('id', 'name', 'category', 'status')

admin.site.register(blogcategory, blogcategoryAdmin)
admin.site.register(blog, blogAdmin)