from django.contrib import admin

#ADMIN MODELS
from .models import Category, PortfolioEntry

admin.site.register(Category)
admin.site.register(PortfolioEntry)