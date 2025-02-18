from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse

from .models import UserAccount
from .forms import UserAccountForm

from checkout.models import Order


def account(request):

    account = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account details updated successfully!')

    form = UserAccountForm(instance=account)
    orders = account.orders.all()

    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
        'account': account,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    order_data = {
        "order_number": order.order_number,
        "date": order.date.strftime("%Y-%m-%d %H:%M:%S"),
        "total": float(order.grand_total),
        "items": [
            {
                "name": item.menu_item.name,
                "price": float(item.menu_item.price),
                "quantity": item.quantity,
            }
            for item in order.lineitems.all()

        ]
    }

    return JsonResponse(order_data)