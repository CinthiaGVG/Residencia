from .models import DojoModel
from bootstrap_modal_forms.forms import BSModalModelForm

class DojoModelForm(BSModalModelForm):
    class Meta:
        model = DojoModel
        fields = ['NombreDojo', 'NombreSensei','Tel']