""" Add forms """
from django import forms
from .models import Subscribe


class SubscribeForm(forms.ModelForm):
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
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True

    class Meta:
        """Add model and fields"""
        model = Subscribe
        fields = ('full_name', 'email')
