from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.contrib import messages

from menu.models import MenuItem

# Create your views here.

def view_bag(request):

    """view shopping bag"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    menu_item = get_object_or_404(MenuItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'You have added {quantity} more {menu_item.name} to your order')

    else:
        bag[item_id] = quantity
        messages.success(request, f'{menu_item.name} added to your order')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):

    menu_item = get_object_or_404(MenuItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'Updated {menu_item.name} quantity to {quantity}')
    else:
        bag.pop[item_id]
        messages.success(request, f'Removed {menu_item.name} from your order')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):

    menu_item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        try:
            bag = request.session.get('bag', {})
            if item_id in bag:
                bag.pop(item_id)
                request.session['bag'] = bag
                messages.success(request, f'Removed {menu_item.name} from your order')
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=404)  # Item not found in the bag
        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)
    return HttpResponseNotAllowed("Only POST method is allowed")
