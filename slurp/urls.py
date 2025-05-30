"""slurp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import custom_404
from django.views.static import serve
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('account/', include('accounts.urls')),
    path('contact/', include('contact.urls')),
    path('bookings/', include('bookings.urls')),
    path('newsletter/', include('newsletter.urls')),
    path("robots.txt", serve, {
        'path': 'robots.txt',
        'document_root': os.path.join(settings.BASE_DIR, 'static'),
    }),

    path("sitemap.xml", serve, {
        'path': 'sitemap.xml',
        'document_root': os.path.join(settings.BASE_DIR, 'static'),
    }),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "home.views.custom_404"
