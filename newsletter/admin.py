from django.contrib import admin
from .models import NewsLetterSubscription

@admin.register(NewsLetterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed')
    search_fields = ('email',)
    ordering = ('-date_subscribed',)
