from django.shortcuts import render, get_object_or_404
from .models import UserAccount
from .forms import UserAccountForm


def account(request):

    
    account = get_object_or_404(UserAccount, user=request.user)
    form = UserAccountForm(instance=account)
    orders = account.orders.all()
    template = 'accounts/account.html'
    context = {
        'form': form,
        'orders': orders,
        'account': account,
    }

    return render(request, template, context)