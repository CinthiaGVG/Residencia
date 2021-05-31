from .models import ParticipanteModel
from django.forms import ModelForm
from django import forms


class ParticipanteModelForm(ModelForm):
    class Meta:
        model = ParticipanteModel
        fields = [ 'Nombre','NumParticipante','FechaNacimiento','Edad','generoModel','Peso','dojoModel','clasificacionKata','clasificacionKumite','nivelKata','nivelKumite']
        widgets = {
            'FechaNacimiento': forms.DateInput(attrs={'type': 'date'},format='%Y-%m-%d')
        }

class ParticipanteModelFormUpdate(ModelForm):
    class Meta:
        model = ParticipanteModel
        fields = "__all__"
        widgets = {
            'FechaNacimiento': forms.DateInput(attrs={'type': 'date'},format='%Y-%m-%d')
        }


