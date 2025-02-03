from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    item_count = 0

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
        # 'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context