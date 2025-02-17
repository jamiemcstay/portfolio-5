from django.contrib import admin
from .models import ContactMessage

# Register your models here.

@admin.register(ContactMessage)
class ContactMessage(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
