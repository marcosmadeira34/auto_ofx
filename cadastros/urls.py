from django.urls import include, path

from .views import ClientCadastroView, ClientConsultaView

urlpatterns = [
        path('cadastro/clientes', ClientCadastroView.as_view(), name='cliente'),
        path('consulta/clientes', ClientConsultaView.as_view(), name='consulta')
        
    ]


