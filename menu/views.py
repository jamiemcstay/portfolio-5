from django.shortcuts import render
from .models import MenuItem, Category

# Create your views here.

def menu(request):

    """ A view to show the menu items
    """

    menu_items = MenuItem.objects.all()


    # Organizing items by category
    categorized_items = {
        "most_popular": menu_items.filter(category__name="most_popular"),
        "starters": menu_items.filter(category__name__iexact="starters"),
        "mains": menu_items.filter(category__name__iexact="mains"),
        "sides": menu_items.filter(category__name__iexact="sides"),
        "soft_drinks": menu_items.filter(category__name__iexact="soft_drinks"),
    }
    

    context = {
        "categorized_items": categorized_items,
    }


    return render(request, 'menu/menu.html', context)