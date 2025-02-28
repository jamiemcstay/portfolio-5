from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .models import MenuItem, Category
from .forms import MenuItemForm


def menu(request):

    """ A view to show the menu items
    """

    menu_items = MenuItem.objects.all()

    categorized_items = {
        "most_popular": menu_items.filter(category__name="most_popular"),
        "starters": menu_items.filter(category__name__iexact="starters"),
        "mains": menu_items.filter(category__name__iexact="mains"),
        "sides": menu_items.filter(category__name__iexact="sides"),
        "soft_drinks": menu_items.filter(category__name__iexact="soft_drinks"),
    }

    formatted_categorized_items = {}
    for category_key, items in categorized_items.items():
        formatted_category_key = category_key.replace('_', ' ').title()
        formatted_categorized_items[formatted_category_key] = items

    context = {
        "categorized_items": formatted_categorized_items,
    }
    return render(request, 'menu/menu.html', context)


@user_passes_test(lambda u: u.is_superuser)
def add_menu_item(request):
    form = MenuItemForm()
    if request.method == "POST":
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item added successfully")
            return redirect('menu')
    else:
        form = MenuItemForm()
    return render(request, 'menu/add_menu_item.html', {'form': form})


@user_passes_test(lambda u: u.is_superuser)
def edit_menu_item(request, item_id):

    menu_item = get_object_or_404(MenuItem, id=item_id)

    if request.method == "POST":
        form = MenuItemForm(request.POST, request.FILES, instance=menu_item)
        if form.is_valid():
            form.save()
            messages.success(request, "Menu item updated successfully")
            return redirect('menu')
    else:
        form = MenuItemForm(instance=menu_item)
    return render(
        request,
        'menu/edit_menu_item.html', {'form': form, 'menu_item': menu_item})


@user_passes_test(lambda u: u.is_superuser)
def delete_menu_item(request, item_id):

    menu_item = get_object_or_404(MenuItem, id=item_id)
    menu_item.delete()
    messages.success(request, "Menu item deleted")
    return redirect('menu')
