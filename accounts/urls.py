from django.urls import path
from .import views


urlpatterns = [
    path('account/', views.account, name='account'),  # Main account page
    path('order_history/<order_number>/', views.order_history, name='order_history'),
]
