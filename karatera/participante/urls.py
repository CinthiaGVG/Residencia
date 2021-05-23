from django.urls import path
from .views import Participante_List,Participante_Create,Participante_Update,Participante_Dojo_List,Participante_Create_Dojo

participante_patterns = ([
    path('', Participante_List.as_view(), name="list"),    
    path('create/', Participante_Create.as_view(), name="create"),
    path('update/<int:pk>', Participante_Update.as_view(), name='update'),
    # Participante Dojo
    path('dojo/<int:pk>', Participante_Dojo_List.as_view(), name='dojolist'),
    path('createparticipante/<int:pk>', Participante_Create_Dojo.as_view(), name="create2"),

], 'participante')