from .models import Page

def page_links(request):
    pages = Page.objects.all()
    return{'pages': pages}