def calcula_media(numeros):
    if not numeros:
        raise ValueError("A lista não pode ser vazia")
    return sum(numeros) / len(numeros)

def test_media_com_valores_positivos():
    assert calcula_media([10, 20, 30]) == 20

def test_media_com_um_valor():
    assert calcula_media([5]) == 5

def test_media_com_negativos():
    assert calcula_media([-10, 0, 10]) == 0

def test_media_lista_vazia():
    import pytest
    with pytest.raises(ValueError):
        calcula_media([])

def test_media_com_valores_flutuantes():
    assert calcula_media([1.5, 2.5, 3.5]) == pytest.approx(2.5)
