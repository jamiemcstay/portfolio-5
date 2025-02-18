from django.urls import path
from .import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('edit/<item_id>/', views.edit_menu_item, name='edit_menu_item'),
    path('delete/<item_id>/', views.delete_menu_item, name='delete_menu_item'),
]
