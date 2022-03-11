import requests
import json

def consulta_cnpj(cnpj):
    url = f"https://www.receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    txt_cnpj_contr = response['cnpj']
 
    return response['cnpj'], response['nome'], response['logradouro'], response['bairro'], response['numero'], response['complemento'], response['municipio'], response['uf'], response['cep']
    tsxt = response['tsxt']
    
    


consulta_cnpj(32181860000165)