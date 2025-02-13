from django.shortcuts import render

# Create your views here.

def account(request):
    template = 'accounts/account.html'
    context = {}

    return render(request, template, context)