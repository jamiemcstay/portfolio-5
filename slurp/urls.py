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
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, MenuItemSitemap

# Sitemaps

sitemaps = {
    'static': StaticViewSitemap,
    'menu': MenuItemSitemap,
}

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

    path('sitemap.xml', sitemap, {'sitemaps': {
        'static': StaticViewSitemap,
        'menu': MenuItemSitemap,
    }}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
