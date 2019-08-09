from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import BlogEntry

def index(request):
    context = {
        "blog_entries": BlogEntry.objects.all()
    }
    return render(request, "blog/index.html", context)

def blog(request, item_id):
    if request.method == "POST":
        markup = request.POST.get("html")
        item_id = request.POST.get("item_id")
        model = request.POST.get("model")
        entry_data = BlogEntry.objects.get(pk=item_id)
        if model == "body":
            entry_data.body = markup
        if model == "summary":
            entry_data.summary = markup
        if model == "title":
            entry_data.title = markup 
        if model == "thumbnail_url":
            entry_data.thumbnail_url = markup
        entry_data.save()
    try:
        entry = BlogEntry.objects.get(pk=item_id)
    except entry.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entry": entry
    }
    return render(request, "blog/blog.html", context)