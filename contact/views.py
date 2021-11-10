"""Import render"""
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def add_contact(request, template='contact/contact.html'):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
            messages.success(request, 'Contact form sent')
        else:
            messages.error(request, 'Contact form not sent.')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
