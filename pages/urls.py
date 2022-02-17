from django.urls import path, include
from .views import AppView, LoginView
from cadastros.views import ClientCadastroView



urlpatterns = [
    path('', LoginView.as_view(), name='inicio'),
    path('app/', AppView.as_view(), name='app'),
    path('app/cadastro/clientes/', ClientCadastroView.as_view(), name='clientes')


]

