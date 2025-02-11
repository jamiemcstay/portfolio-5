from django.shortcuts import render, redirect, reverse, HttpResponse
from django.http import HttpResponse, HttpResponseNotAllowed

# Create your views here.

def view_bag(request):

    """view shopping bag"""
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    
    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop[item_id]

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    if request.method == 'POST':
        try:
            bag = request.session.get('bag', {})
            if item_id in bag:
                bag.pop(item_id)
                request.session['bag'] = bag
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=404)  # Item not found in the bag
        except KeyError:
            return HttpResponse(status=404)  # If something goes wrong
    return HttpResponseNotAllowed("Only POST method is allowed")
