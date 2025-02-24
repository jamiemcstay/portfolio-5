from django import forms
from .models import Booking
from django.core.exceptions import ValidationError


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name',
                  'email',
                  'phone_number',
                  'number_of_people',
                  'reservation_date',
                  'special_requests']
        widgets = {
            # 'reservation_date': forms.DateTimeInput(
            #     attrs={'type': 'datetime-local'}
            #     )
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of People'}),
            'reservation_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local', 'placeholder': 'Select date and time'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Special Requests (optional)'}),
        }

    def clean_reservation_date(self):
        reservation_date = self.cleaned_data['reservation_date']
        number_of_people = self.cleaned_data['number_of_people']

        booking = Booking(
            name=self.cleaned_data['name'],
            email=self.cleaned_data['email'],
            phone_number=self.cleaned_data['phone_number'],
            number_of_people=number_of_people,
            reservation_date=reservation_date
        )

        if not booking.is_time_slot_available():
            raise ValidationError(
                'Sorry we cannot fit this number of people at this time')
        return reservation_date
