from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f"Contact Form Submission from {name}",
                message=f"From: {name} ({email})\n\n{message}",
                from_email='jamiemcstay@hotmail.com',
                recipient_list=['jamiemcstay@hotmail.com'],
                fail_silently=False,
            )

            ContactMessage.objects.create(name=name, email=email,
                                          message=message)

            messages.success(request, 'Your message has been sent')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
