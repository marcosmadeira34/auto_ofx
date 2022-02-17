from django.contrib import admin
from .models import CadastroClientes, CadastroContas

# Register your models here.
admin.site.register(CadastroClientes)
admin.site.register(CadastroContas)