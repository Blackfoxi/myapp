from django.urls import path

from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
]
