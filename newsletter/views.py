from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsLetterForm


def newsletter_signup(request):
    if request.method == "POST":
        newsletter_form = NewsLetterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, "You're subscribed!")
        else:
            messages.error(request, "Invalid email. Please try again")
    return redirect(request.META.get("HTTP_REFERER", "home"))
