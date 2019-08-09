from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bindex'),
    path("<int:item_id>", views.blog, name='blog'),
]