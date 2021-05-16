from .models import ParticipanteModel
from bootstrap_modal_forms.forms import BSModalModelForm

class ParticipanteModelForm(BSModalModelForm):
    class Meta:
        model = ParticipanteModel
        fields = [ 'Nombre','NumParticipante','FechaNacimiento','Edad','generoModel','Peso','dojoModel']



