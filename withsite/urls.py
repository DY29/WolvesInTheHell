from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('fashion/', views.fashion, name='fashion'),
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
    path('travel/', views.travel, name='travel'),
]