from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):     # ModelForm pochodzi z django

    class Meta:
        model = Contact
        fields = '__all__'