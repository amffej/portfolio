from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='findex'),
    path('portfolio/<int:item_id>', views.folio, name='folio'),
    path('about/<int:item_id>', views.about, name='about'),
]