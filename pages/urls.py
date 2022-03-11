from django.urls import path, include
from .views import AppView, LoginView, QueryView
from cadastros.views import ClientCadastroView
from cadastros.views import ClientConsultaView



urlpatterns = [
    path('', LoginView.as_view(), name='inicio'),
    path('app/', AppView.as_view(), name='app'),
    path('app/cadastro/clientes/', ClientCadastroView.as_view(), name='clientes'),
    path('app/consulta/clientes/', ClientConsultaView.as_view(), name='consulta')

]

