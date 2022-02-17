from django.db import models

# Create your models here.
class CadastroClientes(models.Model):
    cnpj_cliente = models.IntegerField()
    token_house = models.IntegerField()
    razao_social = models.CharField(max_length=250, verbose_name='Razão')
    conta = models.IntegerField()
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    numero = models.IntegerField()
    complemento = models.IntegerField()
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=2)
    cep = models.IntegerField()

    
    def __str__(self):
        return "{}({})".format(self.id, self.cnpj_pagador, self.token_house, self.razao_social, 
                              self.conta, self.rua, self.bairro, self.numero, self.complemento, 
                              self.cidade, self.estado, self.cep)            

class CadastroContas(models.Model):
    BANK_CODE = [
        ('001', 'Banco do Brasil'),
        ('033', 'Banco Santander'),
        ('104', 'Caixa Econômica Federal'),
        ('237', 'Banco Bradesco'),
        ('341', 'Banco Itaú'),
        ('748', 'Banco Sicredi'),
        ('756', 'Banco Sicoob')
    ]
    
    cnpj_house = models.IntegerField()
    token_house = models.IntegerField()
    cnpj_cliente = models.IntegerField()
    bank_code = models.IntegerField(choices=BANK_CODE)
    agency = models.IntegerField()
    account = models.IntegerField()

    
    def _str__(self):
        return "{} ({})".format(self.bank_code, self.agency)




    