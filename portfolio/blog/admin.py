from django.contrib import admin

# Register your models here.
from .models import Category, BlogEntry

admin.site.register(Category)
admin.site.register(BlogEntry)