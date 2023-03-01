from .models import Artslice
from django.forms import ModelForm, TextInput


class ArtsliceForm(ModelForm):
    class Meta:
        model = Artslice
        fields = ['id', 'full_name', 'email', 'group']

        widgets = {
            'full_name': TextInput(attrs={
                'placeholder': 'Введите ФИО'}),
            'email': TextInput(attrs={
                 'placeholder': 'Введите почту'}),
            'group': TextInput(attrs={
                'placeholder': 'Введите группу'}),

        }