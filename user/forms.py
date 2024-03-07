from django import forms
from administrator.models import UserComplaint


class UserComplaintForm(forms.ModelForm):
    """Form definition for UserComplaint."""

    class Meta:
        """Meta definition for UserComplaintform."""

        model = UserComplaint
        fields = ['pooler','complaint_text']
