from django import  forms
from django.forms import fields
from  .models import Usuario
from  .models import Turno

class TurnoForms(forms.ModelForm):
    class Meta:
        model=Turno
        fields='__all__'

class UsuariosForms(forms.ModelForm):
    class Meta:
        model=Usuario
        fields='__all__'
