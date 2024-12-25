
from typing import List
from shapely.geometry import shape, Polygon

class AlertaInmet:
    id: int
    id_sequencia: int
    poligono: Polygon

class Alertas:
    hoje: List[AlertaInmet]
    futuro: List[AlertaInmet]
