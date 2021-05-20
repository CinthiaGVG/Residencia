
from django.shortcuts import render
from .models import ParticipanteModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from .forms import ParticipanteModelForm
from administrador.models import GeneroModel

# Create your views here.
class Participante_List(ListView):
    model = ParticipanteModel

class Participante_Create(BSModalCreateView):
    template_name = 'participante/participantemodel_form.html'
    form_class = ParticipanteModelForm
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('participante:list')
    def get_initial(self):
        initial = super(Participante_Create, self).get_initial()
        try:
            generoModel = self.get_object().GeneroModel
        except:
            pass
        else:
            initial['field1'] = GeneroModel.pk          
        return initial
   

class Participante_Update(BSModalUpdateView):
    model = ParticipanteModel
    template_name = 'participante/participantemodel_update.html'
    form_class = ParticipanteModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('participante:list')