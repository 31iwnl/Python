from django import forms
from .models import Artslice


class ArtsliceForm(forms.ModelForm):

    class Meta:
        model = Artslice
        fields = '__all__'
