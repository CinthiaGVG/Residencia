from django.urls import path
from .views import Participante_List,Participante_Create,Participante_Update,Participante_Dojo_List,Create_Dojo,Update_Dojo

participante_patterns = ([
    path('', Participante_List.as_view(), name="list"),    
    path('create/', Participante_Create.as_view(), name="create"),
    path('update/<int:pk>', Participante_Update.as_view(), name='update'),
    # Participante Dojo
    path('dojo/<int:pk>', Participante_Dojo_List.as_view(), name='dojolist'),
    path('createparticipante/<int:pk>', Create_Dojo.as_view(), name="create_dojo"),
    path('updateparticipante/<int:pk>', Update_Dojo, name="update_dojo"),

], 'participante')