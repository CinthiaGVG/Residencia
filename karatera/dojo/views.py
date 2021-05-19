from django.shortcuts import get_list_or_404, render
from .models import DojoModel
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView
from .forms import DojoModelForm

# Create your views here.
class Dojo_List(ListView):    
    model = DojoModel   

class Dojo_Create(BSModalCreateView):
    template_name = 'dojo/dojomodel_form.html'
    form_class = DojoModelForm
    success_message = 'Success: Sign up succeeded. You can now Log in.'
    success_url = reverse_lazy('dojo:list')

class Dojo_Update(BSModalUpdateView):
    model = DojoModel
    template_name = 'dojo/dojomodel_update.html'
    form_class = DojoModelForm
    success_message = 'Success: Book was updated.'
    success_url = reverse_lazy('dojo:list')

class DojoInf_List(ListView):
    template_name = "dojo/dojomodel_inf.html"
    model = DojoModel    
    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        qss = get_list_or_404(qs.filter(pk=self.kwargs['pk']))
        return qss
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query2'] = DojoModel.objects.get(pk=self.kwargs['pk'])
        return context