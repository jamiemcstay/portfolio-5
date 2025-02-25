from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home', 'contact', 'make_booking', 'menu']

    def location(self, item):
        return reverse(item)


class MenuItemSitemap(Sitemap):
    """Sitemap for menu items"""

    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return ['menu']

    def location(self, item):
        return reverse(item)
