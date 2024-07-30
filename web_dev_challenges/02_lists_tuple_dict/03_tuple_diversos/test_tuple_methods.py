from tuple_methods import (
    tuple_sum,
    find_second_element,
    find_out_typle_error,
)
import inspect
import pytest

def test_not_none():
    assert tuple_sum() is not None, "Esperado valor diferente de 'None'"
    assert find_second_element() is not None, "Esperado valor diferente de 'None'"
    assert find_out_typle_error() is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(tuple_sum()) == int, "Esperado um número inteiro"
    assert type(find_second_element()) == int, "Esperado um inteiro"
    assert type(find_out_typle_error()) == tuple, "Esperado uma tupla"

def test_parameters():
    assert len(inspect.getfullargspec(tuple_sum).args) == 0, "Assinatura da função não deverá receber parâmetros"
    assert len(inspect.getfullargspec(find_second_element).args) == 0, "Assinatura da função não deverá receber parâmetros"
    assert len(inspect.getfullargspec(find_out_typle_error).args) == 0, "Assinatura da função não deverá receber parâmetros"

def test_tuple_sum():
    assert tuple_sum() == 15, f"Soma de my_tuple é 15"

def test_find_second_element():
    assert find_second_element() == 2, f"Segundo elemento de my_tupe é 2"

def test_find_out_typle_error():
    my_tuple = 1, 2, 3, 4, 5
    assert find_out_typle_error() == my_tuple, f"Função deverá retornar my_tuple completa"
