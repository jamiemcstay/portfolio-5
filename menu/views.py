from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def menu_items(request):

    """ A view to show the menu items
    """

    menu_items = MenuItem.objects.all()


    context = {
    'menu_items': menu_items,  # Key-value pair for the template
    }


    return render(request, 'menu/menu_items.html', context)