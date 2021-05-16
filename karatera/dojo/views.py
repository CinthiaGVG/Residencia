from django.shortcuts import render
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