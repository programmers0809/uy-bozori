from django import forms
from .models import Contoct

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contoct
        fields = ['name', 'email', 'subject', 'message']  # Formada ishlatiladigan maydonlar
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name...', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email...', 'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject...', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message...', 'class': 'form-control', 'rows': 5}),
        }
