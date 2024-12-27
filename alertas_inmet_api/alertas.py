"""
Módulo da classe Alertas da API de Alertas Meteorológicos do INMET
"""

from alertas_inmet_api import Alerta


class Alertas:
    """
    Representa o conjunto de alertas atuais.

    Atributos:
        hoje(List[Alerta]): lista alertas que acontecerão hoje
        futuro(List[Alerta]): lista de alertas que acontecerão nos próximos dias
    """
    hoje: list[Alerta]
    futuro: list[Alerta]

    def __init__(self, api_json: dict) -> None:
        """
        Inicializa uma nova instância da classe Alertas.

        Args:
            api_json(dict): resultado em json da API de Alertas Meteorológicos do INMET
        """
        self.hoje = []
        for alerta in api_json["hoje"]:
            self.hoje.append(Alerta(alerta))

        self.futuro = []
        for alerta in api_json["futuro"]:
            self.futuro.append(Alerta(alerta))

    def __str__(self) -> str:
        """
        Imprime em formato legível para humanos a classe Alertas

        Returns:
            str: o formato legível para humanos.
        """
        string = 'hoje: \n'
        for alerta in self.hoje:
            string = string + '  - ' + str(alerta) + '\n'
        return string
