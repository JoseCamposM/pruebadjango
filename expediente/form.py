from django import forms
from .models import Expediente

class ExpForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'





