from django.urls import path
from .import views

urlpatterns = [
    path('subscribe/', views.newsletter_signup, name='newsletter_signup'),
]
