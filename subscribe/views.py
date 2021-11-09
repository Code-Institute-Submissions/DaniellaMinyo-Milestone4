from django.shortcuts import render
from .forms import SubscribeForm
from django.contrib import messages


def add_subscription(request, template='subscribe/subscribe.html'):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            form = SubscribeForm()
            messages.success(request, 'Subscribed!')
        else:
            messages.error(request, 'Subscription failed.')
    else:
        form = SubscribeForm()

    template = 'subscribe/subscribe.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
