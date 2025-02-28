from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.utils.timezone import localtime
from django.utils.dateparse import parse_datetime
from .models import Booking


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
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'placeholder': 'Your Email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control',
                                                   'placeholder':
                                                   'Phone Number'}),
            'number_of_people': forms.NumberInput(attrs={'class':
                                                         'form-control',
                                                         'placeholder':
                                                         'Number of People',
                                                         'min': 1, 'max': 30}),
            'reservation_date': forms.DateTimeInput(attrs={'class':
                                                           'form-control',
                                                           'type':
                                                           'datetime-local',
                                                           'placeholder':
                                                           'Select date and \
                                                           time'}),
            'special_requests': forms.Textarea(
                attrs={'class': 'form-control',
                                'rows': 4, 'placeholder':
                                'Special Requests (optional)'}),
        }

    def clean_number_of_people(self):
        """Ensure number of people is between 1 and 30"""
        number_of_people = self.cleaned_data.get('number_of_people', 1)

        if number_of_people < 1:
            raise ValidationError(
                "You must have at least 1 person for the booking")
        if number_of_people > 30:
            raise ValidationError("We cannot accomodate more than 30 people.")

        return number_of_people

    def clean_reservation_date(self):
        """Ensure reservation date is available and in the future"""
        reservation_date = self.cleaned_data['reservation_date']
        number_of_people = self.cleaned_data['number_of_people']

        if not reservation_date:
            raise ValidationError("Please select a reservation date.")

        if isinstance(reservation_date, str):
            reservation_date = parse_datetime(reservation_date)
            if reservation_date is None:
                raise ValidationError(
                    "Invalid date format. Please use correct format.")

        print(f"reservation_date: {reservation_date}")
        print(timezone.now())

        if reservation_date < localtime(timezone.now()):
            raise ValidationError("Please pick a date starting from today.")

        total_people_at_time = sum(
            booking.number_of_people
            for booking in Booking.objects.filter(
                reservation_date=reservation_date))

        if total_people_at_time + number_of_people > 30:
            raise ValidationError(
                "Sorry, we cannot accomodate that number \
                of people at this time.")

        return reservation_date
