from django.shortcuts import render, get_object_or_404
from . models import blog, blogcategory

# Create your views here.

def blogs(request):
    all_blogs = blog.objects.all()
    return render(request, 'blogs/blogs1.html', {'blogs': all_blogs})

def blog_detail(request, id):
    blog_details = get_object_or_404(blog, id=id)
    return render(request, 'blogs/details1.html', {'Blog': blog_details})