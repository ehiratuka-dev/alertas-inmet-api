import pytest
# from alertas_inmet_api import torre_hanoi
from alertas_inmet_api.hanoi import torre_hanoi

def test_torre_hanoi():
    # Chama a função torre_hanoi com 3 discos
    movimentos = torre_hanoi(3, 'A', 'C', 'B')

    # Define o resultado esperado
    expected_result = [
        "Move o disco 1 de A para C",
        "Move o disco 2 de A para B",
        "Move o disco 1 de C para B",
        "Move o disco 3 de A para C",
        "Move o disco 1 de B para A",
        "Move o disco 2 de B para C",
        "Move o disco 1 de A para C"
    ]

    # Compara o resultado gerado com o esperado
    assert movimentos == expected_result