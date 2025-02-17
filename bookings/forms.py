from django import forms
from .models import Booking
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone_number', 'number_of_people', 'reservation_date', 'special_requests']
        widgets = {
            'reservation_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data['reservation_date']
        number_of_people = self.cleaned_data['number_of_people']

        booking = Booking(name=self.cleaned_data['name'], email=self.cleaned_data['email'],
                          phone_number=self.cleaned_data['phone_number'], number_of_people=number_of_people,
                          reservation_date=reservation_date)

        if not booking.is_time_slot_available():
            raise ValidationError('Sorry we cannot fit this number of people at this time')
        return reservation_date
