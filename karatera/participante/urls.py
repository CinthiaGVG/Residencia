from django.urls import path
from .views import Participante_Create,Participante_List,Participante_Update

participante_patterns = ([
    path('', Participante_List.as_view(), name="list"),    
    path('create/', Participante_Create.as_view(), name="create"),
    path('update/<int:pk>', Participante_Update.as_view(), name='update'),
], 'participante')