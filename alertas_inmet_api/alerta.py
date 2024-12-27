"""
Módulo da classe Alerta da API de Alertas Meteorológicos do INMET
"""

import json
import re

from datetime import datetime, date, time
from shapely.geometry import shape, Polygon


class Alerta:
    """
    Representa um alerta

    Atributos:
        id(int): código do alerta
        id_aviso(int): código do aviso
        id_sequencia(int): sequencial do código do alerta
        id_condicao_severa(int): código do tipo de condição
        id_icone(int): código do icone
        id_usuario(int): código do usuario
        codigo(str): codigo em formato texto
        referencia(str):
        data_inicio(date): data inicial do alerta
        hora_inicio(time): hora inicial do alerta
        data_fim(date): data final do alerta
        hora_fim(time): data final do alerta
        municipios(list[str]): lista de municipios afetadas
        microrregioes(list[str]): lista de microregioes afetadas
        mesorregioes(list[str]): lista de mesoregioes afetadas
        estados(list[str]): lista de estados afetados
        regioes(list[str]): lista de regioes afetadas
        geocodes(list[str]): geocodes das cidades afetadas
        alterado(bool): flag informando se o alerta foi alterado
        encerrado(bool): flag informando se o alerta foi encerrado
        created_at(datetime): data/hora da criação do alerta
        updated_at(datetime): data/hora da ultima alteração do alerta
        inicio(datetime): data/hora inicial do alerta
        fim(datetime): data/hora final do alerta
        poligono(Polygon): poligono descrevendo a área impactada pelo alerta
        icone(str): imagem em formato binário do icone do alerta
        descricao(str): descrição do tipo de condição
        aviso_cor(str): cor do alerta de acordo com a severidade
        id_severidade(int): código da severidade
        severidade(str): descrição da severidade
        riscos(list[str]): lista com os riscos que a condição pode causar
        instrucoes(list[str]): lista de instruções para se proteget da condicao
    """
    id: int
    id_aviso: int
    id_sequencia: int
    id_condicao_severa: int
    id_icone: int
    id_usuario: int
    codigo: str
    referencia: str
    data_inicio: date
    hora_inicio: time
    data_fim: date
    hora_fim: time
    municipios: list[str]
    microrregioes: list[str]
    mesorregioes: list[str]
    estados: list[str]
    regioes: list[str]
    geocodes: list[str]
    alterado: bool
    encerrado: bool
    created_at: datetime
    updated_at: str
    inicio: str
    fim: str
    poligono: Polygon
    icone: str
    descricao: str
    aviso_cor: str
    id_severidade: int
    severidade: str
    riscos: list[str]
    instrucoes: list[str]

    def __init__(self, alerta_json: dict) -> None:
        """
        Inicializa uma nova instância da classe Alerta.

        Args:
            alerta_json(dict): resultado em json do alerta da
            API de Alertas Meteorológicos do INMET
        """
        self.id = alerta_json["id"]
        self.id_aviso = alerta_json["id_aviso"]
        self.id_sequencia = alerta_json["id_sequencia"]
        self.id_condicao_severa = alerta_json["id_condicao_severa"]
        self.id_icone = alerta_json["id_icone"]
        self.id_usuario = alerta_json["id_usuario"]
        self.codigo = alerta_json["codigo"]
        self.referencia = alerta_json["referencia"]
        self.data_inicio = datetime.strptime(
            alerta_json["data_inicio"], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        self.data_fim = datetime.strptime(
            alerta_json["data_fim"], "%Y-%m-%dT%H:%M:%S.%fZ").date()
        self.hora_inicio = datetime.strptime(
            alerta_json["hora_inicio"], "%H:%M").time()
        self.hora_fim = datetime.strptime(
            alerta_json["hora_fim"], "%H:%M").time()
        self.municipios = [
            municipio for municipio in alerta_json["municipios"].split(",")]
        self.microrregioes = [
            microregiao for microregiao in alerta_json["microrregioes"].split(",")]
        self.mesorregioes = [
            macroregiao for macroregiao in alerta_json["mesorregioes"].split(",")]
        self.estados = [estado for estado in alerta_json["estados"].split(",")]
        self.regioes = [regiao for regiao in alerta_json["regioes"].split(",")]
        self.geocodes = [geocode for geocode in alerta_json["geocodes"].split(",")]
        self.alterado = alerta_json["alterado"]
        self.encerrado = alerta_json["encerrado"]
        self.created_at = datetime.strptime(
            alerta_json["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.updated_at = datetime.strptime(
            alerta_json["updated_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        self.inicio = datetime.strptime(
            alerta_json["inicio"], "%Y-%m-%d %H:%M")
        self.fim = datetime.strptime(
            alerta_json["fim"], "%Y-%m-%d %H:%M")
        self.poligono = shape(json.loads(alerta_json["poligono"]))
        self.icone = re.sub(r"^data:image/[^;]+;base64,", "", alerta_json["icone"])
        self.descricao = alerta_json["descricao"]
        self.aviso_cor = alerta_json["aviso_cor"]
        self.id_severidade = alerta_json["id_severidade"]
        self.severidade = alerta_json["severidade"]
        self.riscos = list(alerta_json["riscos"])
        self.instrucoes = list(alerta_json["instrucoes"])

    def format_value(self, key: str, value: str) -> str:
        """
        Escolhe o melhor método para representar uma classe

        Args:
            key(str): nome da chave que o dado está armazenado
            value(str): valor do dado armazenado

        Returns:
            str: o formato legível para humanos de uma chave.
        """
        key_string = f"{key}: "
        if isinstance(value, list):
            key_string = key_string + "\n        " + \
                "\n        ".join(str(item) for item in value[:5])
        else:
            key_string = key_string + str(value)
        return key_string

    def __str__(self) -> str:
        """
        Imprime em formato legível para humanos a classe Alerta

        Returns:
            str: o formato legível para humanos.
        """
        key_string = ''
        for key, value in ((k, v) for k, v in vars(self).items()
                           if k not in ['icone', 'poligono']):
            key_string = key_string + self.format_value(key, value) + "\n    "
        return key_string
