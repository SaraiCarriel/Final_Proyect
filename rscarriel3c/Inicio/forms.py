from django import forms
from django.forms import ModelChoiceField, Select
from .models import Donacion, Ciudad, Beneficiario, Categoria


class DonaForm(forms.ModelForm):
    class Meta:
        model = Donacion
        fields = ['nombre', 'monto', 'categoria', 'ciudad', 'persona', 'correo']
        widgets = {'nombre':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Su Nombre',}),
		'monto':forms.NumberInput(attrs={'class': 'form-control','placeholder':'Ingrese el monto a Donar',}),
		'categoria':forms.Select(attrs={'class': 'form-control'}),
		'correo':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese un Correo',}),
		'ciudad': forms.Select(attrs={'class': 'form-control'}),
		'persona':forms.Select(attrs={'class': 'form-control'})
		}