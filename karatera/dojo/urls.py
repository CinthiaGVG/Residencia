from django.urls import path
from .views import Dojo_Create,Dojo_List,Dojo_Update,DojoInf_List

dojo_patterns = ([
    
    path('', Dojo_List.as_view(), name="list"),    
    path('create/', Dojo_Create.as_view(), name="create"),
    path('update/<int:pk>', Dojo_Update.as_view(), name='update'),
    path('<int:pk>/', DojoInf_List.as_view(), name='view'),
], 'dojo')