from django.urls import path
from .import views


urlpatterns = [
    path('', views.make_booking, name='make_booking'),
]
