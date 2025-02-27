from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    number_of_people = models.IntegerField()
    reservation_date = models.DateTimeField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(30)]
    )
    special_requests = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), (
            'cancelled', 'Cancelled')],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.name} on {self.reservation_date}"

    def is_time_slot_available(self):
        bookings_at_time = Booking.objects.filter(reservation_date=self
                                                  .reservation_date)
        total_people = sum([booking.number_of_people for booking in
                            bookings_at_time])
        return total_people + self.number_of_people <= 30
