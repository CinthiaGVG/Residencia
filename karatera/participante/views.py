
from django.shortcuts import get_list_or_404,render,get_object_or_404
from .models import ParticipanteModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalFormView
from .forms import ParticipanteModelForm
from administrador.models import GeneroModel
# Dojo
from dojo.models import DojoModel

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

# [I] Participante-Dojo
class Participante_Dojo_List(ListView):
    template_name = 'participante/participante_dojo_list.html'
    model = DojoModel
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        qss = get_object_or_404(qs.filter(pk=self.kwargs['pk']))
        return qss
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['QueryParticipante'] = ParticipanteModel.objects.filter(dojoModel=self.kwargs['pk'])
        return context

class Participante_Create_Dojo(BSModalCreateView):
    template_name = 'participante/participante_dojo_form.html'
    form_class = ParticipanteModelForm    
    def get_initial(self):
        initial = super(Participante_Create_Dojo, self).get_initial()
        initial['dojoModel'] = self.kwargs['pk']
        return initial
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        data = form.data.copy()
        data['nivelKata'] = 2
        data['nivelKumite'] = 2
        data['clasificacionKata'] = 2
        data['clasificacionKumite'] = 2
        form.data=data        
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(self, form)
    def get_success_url(self, *args, **kwargs):    
        return reverse_lazy('participante:dojolist', kwargs={'pk':self.kwargs['pk']})
    def form_invalid(self, form):
       """If the form is invalid, render the invalid form."""
       return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
        return super().get_context_data(**kwargs)
 
        
   
# [F] Participante-Dojo
