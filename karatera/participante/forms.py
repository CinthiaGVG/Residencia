from .models import ParticipanteModel
from django.forms import ModelForm

class ParticipanteModelForm(ModelForm):
    class Meta:
        model = ParticipanteModel
        fields = [ 'Nombre','NumParticipante','FechaNacimiento','Edad','generoModel','Peso','dojoModel','clasificacionKata','clasificacionKumite','nivelKata','nivelKumite']



