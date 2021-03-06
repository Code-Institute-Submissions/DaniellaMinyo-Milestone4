from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Add custom default value to email field """

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

    class Meta:
        """Add model and fields"""
        model = Contact
        fields = ('full_name', 'email', 'subject', 'message')
