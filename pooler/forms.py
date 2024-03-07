from django import forms
from .models import Car

class CarForm(forms.ModelForm):
    """Form definition for Car."""

    class Meta:
        """Meta definition for Carform."""

        model = Car
        exclude = ['owner', 'status']
        widgets = {
            'reg_no': forms.TextInput(attrs={
                'pattern': '^[A-Z]{2}\s[0-9]{1, 2}\s[A-Z]{2}\s[0-9]{4}$'
            })
        }

class CarEditForm(forms.ModelForm):
    """Form definition for Car."""

    class Meta:
        """Meta definition for Carform."""

        model = Car
        exclude = ['owner', 'status', 'luggage_capacity', 'reg_no']
