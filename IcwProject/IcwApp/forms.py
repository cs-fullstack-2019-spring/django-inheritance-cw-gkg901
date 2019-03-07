from django import forms
from .models import contactModel


class contactForm(forms.ModelForm):
    class Meta:
        model = contactModel
        fields = '__all__'
