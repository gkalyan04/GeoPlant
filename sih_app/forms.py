from django import forms
from django.core import validators
from sih_app.models import Plant


class NewUserForm(forms.ModelForm):
    class Meta():
        model = Plant 
        fields = '__all__'



