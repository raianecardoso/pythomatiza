from desafios_list_tuple import (
    days_in_a_month,
    calory_counter,
)
import inspect
import pytest

def test_not_none():
    assert days_in_a_month('Janeiro') is not None, "Esperado valor diferente de 'None'"
    assert calory_counter('Hamburger', 'French Fries', 'Sprite') is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(days_in_a_month('Janeiro')) == int, "Esperado um número inteiro"
    assert type(calory_counter('Hamburger', 'French Fries', 'Sprite')) == int, "Esperado um dicionário"

def test_parameters():
    assert len(inspect.getfullargspec(days_in_a_month).args) == 1, "Assinatura da função deverá receber 1 parâmetro"
    assert len(inspect.getfullargspec(calory_counter).args) == 3, "Assinatura da função deverá receber 2 parâmetros"

@pytest.mark.parametrize("month, expected_result", [
    ('Janeiro', 31),
    ('Fevereiro', 28),
    ('Março', 31),
    ('Abril', 30),
    ('Maio', 31),
    ('Junho', 30),
    ('Julho', 31),
    ('Agosto', 31),
    ('Setembro', 30),
    ('Outubro', 31),
    ('Novembro', 30),
    ('Dezembro', 31),
])
def test_days_in_a_month(month, expected_result):
    assert days_in_a_month(month) == expected_result, f"{month} tem {expected_result} dias"


@pytest.mark.parametrize("first_item, second_item, third_item, expected_result", [
    ('Hamburger', 'French Fries', 'Sprite', 630),
    ('Cheese Bacon Egg', 'French Fries', 'Coca Cola', 920),
    ('Salad', 'French Fries', 'Sprite', 395),
])
def test_calory_counter(first_item, second_item, third_item, expected_result):
    assert calory_counter(first_item, second_item, third_item) == expected_result, f"As calorias de {first_item}, {second_item} e {third_item} são iguais a {expected_result}"
