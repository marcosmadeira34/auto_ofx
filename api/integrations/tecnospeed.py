import os 
from constants import TOKENSH, CNPJSH, PAYERCPFCNPJ, URL_PROD  
import requests
from urllib.parse import urljoin
import json
    

class Tecnolog:    
    def __init__(self, ):
        self.tokensh =  TOKENSH
        self.cnpjsh = CNPJSH
        self.payercpfcnpj = CNPJSH
        self.url = URL_PROD

    

    """cadastrar pagador"""
    def register_payer():
        url_post = urljoin((URL_PROD, f'/parser'))
        header = {
            "cnpjsh": CNPJSH,
            "tokensh": TOKENSH,
            "Accept":"application/json",
            "ContentType":"application/json"
        }

        request = requests.post(url_post, header=header)
        return requests.Response(json.dumps(request), 201, content_type="application/json")











