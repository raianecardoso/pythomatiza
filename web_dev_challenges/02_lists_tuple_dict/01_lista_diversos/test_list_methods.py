from list_methods import (
    sort_asc,
    sort_desc,
    find_list_element,
    find_last_list_element,
    find_out_of_range_error,
    x_not_in_the_list_error,
    list_remove_last,
)
import inspect
import pytest

my_list = ['Gabriel', 'Davi', 'Ana']

def test_not_none():
    assert sort_asc(my_list) is not None, "Esperado valor diferente de 'None'"
    assert sort_desc(my_list) is not None, "Esperado valor diferente de 'None'"
    assert find_list_element(my_list) is not None, "Esperado valor diferente de 'None'"
    assert find_last_list_element(my_list) is not None, "Esperado valor diferente de 'None'"
    assert find_out_of_range_error() is not None, "Esperado valor diferente de 'None'"
    assert x_not_in_the_list_error() is not None, "Esperado valor diferente de 'None'"
    assert list_remove_last(my_list) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(sort_asc(my_list)) == list, "Esperado uma lista"
    assert type(sort_desc(my_list)) == list, "Esperado uma lista"
    assert type(find_list_element(my_list)) != list, "Esperado valor diferente de uma lista"
    assert type(find_last_list_element(my_list)) != list, "Esperado valor diferente de uma lista"
    assert type(find_out_of_range_error()) != list, "Esperado valor diferente de uma lista"
    assert type(x_not_in_the_list_error()) != list, "Esperado valor diferente de uma lista"
    assert type(list_remove_last(my_list)) == list, "Esperado uma lista"

def test_parameters():
    assert len(inspect.getfullargspec(sort_asc).args) == 1, "Assinatura da função deverá receber um parâmetros"
    assert len(inspect.getfullargspec(sort_desc).args) == 1, "Assinatura da função deverá receber um parâmetros"
    assert len(inspect.getfullargspec(find_list_element).args) == 1, "Assinatura da função deverá receber um parâmetros"
    assert len(inspect.getfullargspec(find_last_list_element).args) == 1, "Assinatura da função deverá receber um parâmetros"
    assert len(inspect.getfullargspec(find_out_of_range_error).args) == 0, "Assinatura da função não deverá receber nenhum parâmetro"
    assert len(inspect.getfullargspec(x_not_in_the_list_error).args) == 0, "Assinatura da função não deverá receber nenhum parâmetro"
    assert len(inspect.getfullargspec(list_remove_last).args) == 1, "Assinatura da função deverá receber um parâmetros"

@pytest.mark.parametrize("my_list, expected_result", [
    ([3,2,1], [1,2,3]),
    (['Gabriel', 'Davi', 'Ana'], ['Ana', 'Davi', 'Gabriel']),
    (['Ana', 'Davi', 'Gabriel'], ['Ana', 'Davi', 'Gabriel']),
    (['Zoológico', 'Parque', 'Jardim'], ['Jardim', 'Parque', 'Zoológico']),
])
def test_sort_asc(my_list, expected_result):
    assert sort_asc(my_list) == expected_result, f"{my_list} classificado em ordem ascendente {expected_result}"


@pytest.mark.parametrize("my_list, expected_result", [
    ([1,2,3], [3,2,1]),
    (['Ana', 'Davi', 'Gabriel'], ['Gabriel', 'Davi', 'Ana']),
    (['Jardim', 'Parque', 'Zoológico'], ['Zoológico', 'Parque', 'Jardim']),
])
def test_sort_desc(my_list, expected_result):
    assert sort_desc(my_list) == expected_result, f"{my_list} classificado em ordem ascendente {expected_result}"

@pytest.mark.parametrize("my_list, expected_result", [
    ([1,2,3], 2),
    (['Ana', 'Davi', 'Gabriel'], 'Davi'),
    (['Jardim', 'Parque', 'Zoológico'], 'Parque'),
])
def test_find_list_element(my_list, expected_result):
    assert find_list_element(my_list) == expected_result, f"O segundo elemento da lista {my_list} é {expected_result}"

@pytest.mark.parametrize("my_list, expected_result", [
    ([1,2,3], 3),
    (['Ana', 'Davi', 'Gabriel'], 'Gabriel'),
    (['Jardim', 'Parque', 'Zoológico'], 'Zoológico'),
])
def test_find_last_list_element(my_list, expected_result):
    assert find_last_list_element(my_list) == expected_result, f"O último elemeento da lista {my_list} é {expected_result}"

def test_find_out_of_range_error():
    assert find_out_of_range_error() in [1, 2, 3, 4, 5] , f"Esperado algum elemento da lista [1, 2, 3, 4, 5]"

def test_x_not_in_the_list_error():
    assert x_not_in_the_list_error() in [1, 2, 3, 4, 5] , f"Esperado algum elemento da lista [1, 2, 3, 4, 5]"

@pytest.mark.parametrize("my_list, expected_result", [
    ([1,2,3], [1,2]),
    (['Ana', 'Davi', 'Gabriel'], ['Ana', 'Davi']),
    (['Jardim', 'Parque', 'Zoológico'], ['Jardim', 'Parque']),
])
def test_list_remove_last(my_list, expected_result):
    assert list_remove_last(my_list) == expected_result, f"A lista {my_list} sem seu último elemento é igual a {expected_result}"
