from django.shortcuts import render
from .models import MenuItem

# Create your views here.

def menu(request):

    """ A view to show the menu items
    """

    menu_items = MenuItem.objects.all()


    # Organizing items by category
    categorized_items = {
        "most_popular": menu_items.filter(category__name="Most Popular"),
        "starters": menu_items.filter(category__name__iexact="Starters"),
        "mains": menu_items.filter(category__name__iexact="Mains"),
        "sides": menu_items.filter(category__name__iexact="Sides"),
        "soft_drinks": menu_items.filter(category__name__iexact="Soft Drinks"),
    }

    print("All Menu Items:", menu_items)
    print("Starters:", menu_items.filter(category__name="Starters"))

    context = {
        "categorized_items": categorized_items,
    }


    return render(request, 'menu/menu.html', context)