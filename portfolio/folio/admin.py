from django.contrib import admin

#ADMIN MODELS
from .models import Category, PortfolioEntry, AboutEntry

admin.site.register(Category)
admin.site.register(PortfolioEntry)
admin.site.register(AboutEntry)