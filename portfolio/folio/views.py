from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        "blank": "none"
    }
    return render(request, "folio/index.html", context)

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