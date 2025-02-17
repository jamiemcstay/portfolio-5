from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

# Create your views here.

def make_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()

            send_mail(
                subject=f"Booking Confirmation for {booking.name}",
                message=f"Dear {booking.name},\n\nYour booking for {booking.number_of_people} on {booking.reservation_date} confirmed.\n\n Special Requests: {booking.special_requests}.\n\nThanks you for choosing Slurp Ramen.",
                from_email='jamiemcstay@hotmail.com',
                recipient_list=[booking.email],
                fail_silently=False,
            )

            messages.success(request, "Your booking has been made successfully!")
            return redirect('make_booking')
    else:
        form = BookingForm()
    return render(request, 'bookings/make_booking.html', {'form': form})
