from django import forms
from .models import Subscribe


class SubscribeForm(forms.ModelForm):
    """Add custom default value to email field """
    email = forms.EmailField(
        label='', widget=forms.EmailInput(
            attrs={'placeholder': 'Your email', 'class': 'form-control'}))
    self.fields['full_name'].widget.attrs['autofocus'] = True

    class Meta:
        """Add model and fields"""
        model = Subscribe
        fields = ('email', 'full_name')
