from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import BlogEntry


def index(request):
    context = {
        "blog_entries": BlogEntry.objects.all()
    }
    return render(request, "blog/index.html", context)

def blog(request, item_id):
    try:
        entry = BlogEntry.objects.get(pk=item_id)
    except entry.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entry": entry
    }
    return render(request, "blog/blog.html", context)