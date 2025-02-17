from django.urls import path
from .import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('add/', views.add_menu_item, name='add_menu_item'),
]