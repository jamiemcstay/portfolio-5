from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from bag.contexts import bag_contents

import stripe

# Create your views here.

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "You have not ordered any food yet")
        return redirect(reverse('menu'))
    
    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 
        'pk_test_51QidLdLuli0zS0QyTA7qHUIvUCp8DltnkWKQCXzdAJrVBbjhzXvkgGKpZqnDyV6Xox47SUFsICHBWChSYe64tllx00yVXdlo41',
        'client_secret': 'test client_secret',
    }

    return render(request,template, context)
