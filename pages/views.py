from re import template
from django.views.generic import TemplateView



# Create your views here.

class LoginView(TemplateView):
    template_name = 'login.html'

class AppView(TemplateView):
    template_name = 'application.html'

class QueryView(TemplateView):
    template_name = 'query.html'