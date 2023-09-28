from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-field'}),
            'email': forms.EmailInput(attrs={'class': 'custom-field'}),
            'subject': forms.TextInput(attrs={'class': 'custom-field'}),
            'message': forms.Textarea(attrs={'class': 'custom-field'}),
        }
