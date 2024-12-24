def torre_hanoi(n, origem, destino, auxiliar):
    """
    Resolve o problema da Torre de Hanoi e retorna os movimentos.

    :param n: número de discos
    :param origem: a torre de onde os discos vão ser movidos
    :param destino: a torre para onde os discos vão ser movidos
    :param auxiliar: a torre auxiliar
    :return: lista com os movimentos
    """
    movimentos = []

    if n == 1:
        movimentos.append(f"Move o disco 1 de {origem} para {destino}")
    else:
        movimentos.extend(torre_hanoi(n-1, origem, auxiliar, destino))
        movimentos.append(f"Move o disco {n} de {origem} para {destino}")
        movimentos.extend(torre_hanoi(n-1, auxiliar, destino, origem))

    return movimentos
