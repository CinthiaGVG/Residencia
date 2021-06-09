from django.urls import path

from . import views

core_patterns = ([
   
    path('', views.home, name='home'),
    path('', views.conducta, name='conducta'),
    path('', views.juzgar, name='juzgar'),
    path('', views.fotos, name='fotos'),

], 'core')