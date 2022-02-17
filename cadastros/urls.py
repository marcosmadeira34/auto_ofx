from django.urls import path, include 
from .views import ClientCadastroView

urlpatterns = [
        path('cadastro/clientes', ClientCadastroView.as_view(), name='cliente')
        
    ]


