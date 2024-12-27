"""
Representa um alerta.
"""
import requests

from alertas_inmet_api import Alertas

URL = "https://apiprevmet3.inmet.gov.br/avisos/ativos"
response = requests.get(URL, timeout=5)

alertas = Alertas(response.json())
print(alertas)
