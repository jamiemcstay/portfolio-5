from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem


def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        menu_item = get_object_or_404(MenuItem, pk=item_id)
        total += quantity * menu_item.price
        item_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'menu_item': menu_item,
        })

    if total > 0:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
