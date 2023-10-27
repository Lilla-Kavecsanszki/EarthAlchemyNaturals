from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'custom-field',
                                           'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'custom-field',
                                             'placeholder': 'Email'}),
            'subject': forms.TextInput(attrs={'class': 'custom-field',
                                              'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'custom-field',
                                             'placeholder': 'Message'}),
        }
