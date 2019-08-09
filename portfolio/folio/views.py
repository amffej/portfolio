from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import PortfolioEntry, AboutEntry

def index(request):
    context = {
        "portfolio_entries": PortfolioEntry.objects.all()
    }
    return render(request, "folio/index.html", context)

def folio(request, item_id):
    if request.method == "POST":
        markup = request.POST.get("html")
        item_id = request.POST.get("item_id")
        model = request.POST.get("model")
        entry_data = PortfolioEntry.objects.get(pk=item_id)
        if model == "body":
            entry_data.body = markup
            entry_data.save()
        if model == "headline":
            entry_data.headline = markup
            entry_data.save()
        if model == "picture_url":
            entry_data.picture_url = markup
            entry_data.save()
    try:
        entry = PortfolioEntry.objects.get(pk=item_id)
    except entry.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entry": entry
    }
    return render(request, "folio/folio.html", context)

def about(request, item_id):
    if request.method == "POST":
        markup = request.POST.get("html")
        item_id = request.POST.get("item_id")
        model = request.POST.get("model")
        entry_data = AboutEntry.objects.get(pk=item_id)
        if model == "body":
            entry_data.body = markup
            entry_data.save()
        if model == "title":
            entry_data.title = markup
            entry_data.save()
    try:
        entry = AboutEntry.objects.get(pk=item_id)
    except entry.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entry": entry
    }
    return render(request, "folio/about.html", context)