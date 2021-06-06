from django.shortcuts import render
from django.http import HttpResponse

    
def home(request):
    return render(request,'core/home.html')

def conducta(request):
    return render(request,'core/conducta.html')

def juzgar(request):
    return render(request,'core/uzgar.html')

def fotos(request):
    return render(request,'core/fotos.html')            