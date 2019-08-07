from django.shortcuts import render
from django.http import HttpResponse, Http404
from . models import PortfolioEntry


def index(request):
    context = {
        "portfolio_entries": PortfolioEntry.objects.all()
    }
    return render(request, "folio/index.html", context)

def folio(request, item_id):
    try:
        entry = PortfolioEntry.objects.get(pk=item_id)
    except entry.DoesNotExist:
        raise Http404("Entree does not exist")
    context = {
        "entry": entry
    }
    return render(request, "folio/folio.html", context)


def contact(request):
    context = {
        "blank": "none"
    }
    return render(request, "folio/contact.html", context)

def about(request):
    context = {
        "blank": "none"
    }
    return render(request, "folio/about.html", context)

def admin(request):
    return HttpResponse("Admin Page")