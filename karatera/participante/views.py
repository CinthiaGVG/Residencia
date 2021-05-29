
from django.shortcuts import get_list_or_404,render,get_object_or_404
from .models import ParticipanteModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalFormView
from .forms import ParticipanteModelForm
from administrador.models import ClasificacionKarateModel, DisciplinaModel, EdadModel, GeneroModel
from django.http import JsonResponse
from django.views.generic.edit import FormView
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

class Participante_Create_Dojo(FormView):
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
        # Disciplina 1 Kata, 2 Kumite
        Edad = data['Edad']
        Genero = data['generoModel']
        m = ClasificacionKarateModel.objects.filter(edadModel__Minimo=Edad)
        print(m)
        data['nivelKata'] = 2
        data['nivelKumite'] = 2
        data['clasificacionKata'] = 2
       # data['clasificacionKumite'] = 2
        form.data=data                
            #return self.form_invalid(form)
        #    return render(request, 'participante/participante_dojo_form.html', {'form': form},status=400)
        #else:
        if form.is_valid():
            return render(request, 'participante/participante_dojo_form.html', {'form': form},status=400)
            #return self.form_valid(form)    
        else:
            return render(request, 'participante/participante_dojo_form.html', {'form': form},status=400)            
    def form_valid(self, form):
        """
        If the form is valid return HTTP 200 status 
        code along with name of the user
        """
        name = form.cleaned_data['Nombre']
        form.save()
        return JsonResponse({"name": name}, status=200)

    def form_invalid(self, form):
        """
        If the form is invalid return status 400
        with the errors.
        """
        errors = form.errors.as_json()
        return JsonResponse({"errors": errors}, status=400)


class Participante_Create_Dojo2(BSModalCreateView):
    template_name = 'participante/participante_dojo_form.html'
    form_class = ParticipanteModelForm    
    def get_initial(self):
        initial = super(Participante_Create_Dojo2, self).get_initial()
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

    # def get_context_data(self, **kwargs):
    #     """Insert the form into the context dict."""
    #     if 'form' not in kwargs:
    #         kwargs['form'] = self.get_form()
    #     return super().get_context_data(**kwargs)
 
        
   
# [F] Participante-Dojo
