from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'reservation_date', 'status', 'number_of_people')
    list_filter = ('status', 'reservation_date')
    search_fields = ('name', 'email', 'phone_number')
