from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='findex'),
    path("portfolio/<int:item_id>", views.folio, name='folio'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('fadmin/<int:item_id>', views.admin, name='admin'),

]