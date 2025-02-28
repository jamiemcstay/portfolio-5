from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
