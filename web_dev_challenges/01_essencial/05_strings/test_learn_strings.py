from learn_strings import (
    has_letter,
    uper_case,
    lower_case,
    capitalize,
    reverse,
)
import inspect
import pytest

def test_not_none():
    assert has_letter('a', 'gabriel') is not None, "Esperado valor diferente de 'None'"
    assert uper_case('sirius') is not None, "Esperado valor diferente de 'None'"
    assert lower_case('sirius') is not None, "Esperado valor diferente de 'None'"
    assert capitalize('sirius') is not None, "Esperado valor diferente de 'None'"
    assert reverse('sirius') is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(has_letter('a', 'gabriel')) == bool, "Esperado valor booleano"
    assert type(uper_case('sirius')) == str , "Esperado valor numérico"
    assert type(lower_case('sirius')) == str, "Esperado valor numérico"
    assert type(capitalize('sirius')) == str, "Esperado valor numérico"
    assert type(reverse('sirius')) == str, "Esperado valor numérico"

def test_parameters():
    assert len(inspect.getfullargspec(has_letter).args) == 2, "Assinatura da função deverá receber dois parâmetros"
    assert len(inspect.getfullargspec(uper_case).args) == 1, "Assinatura da função deverá receber um parâmetros"
    assert len(inspect.getfullargspec(lower_case).args) == 1, "Assinatura da função deverá receber dois parâmetros"
    assert len(inspect.getfullargspec(capitalize).args) == 1, "Assinatura da função deverá receber um parâmetros"
    assert len(inspect.getfullargspec(reverse).args) == 1, "Assinatura da função deverá receber dois parâmetros"

@pytest.mark.parametrize("letter, input_word, expected_result", [
    ('d', 'Davi', False),
    ('D', 'Davi', True),
    ('G', 'Gabriel', True),
    ('i', 'input', True),
])
def test_has_letter(letter, input_word, expected_result):
    assert has_letter(letter, input_word) == expected_result, f"{input_word} contém {letter}: {expected_result}"

@pytest.mark.parametrize("input_word, expected_result", [
    ('gabriel', 'GABRIEL'),
    ('davi', 'DAVI'),
    ('python', 'PYTHON'),
])
def test_uper_case(input_word, expected_result):
    assert uper_case(input_word) == expected_result, f"{input_word} com todas as letras maiúsculas é igual a {expected_result}"

@pytest.mark.parametrize("input_word, expected_result", [
    ('GABRIEL', 'gabriel'),
    ('DAVI', 'davi'),
    ('PYTHON', 'python'),
])
def test_lower_case(input_word, expected_result):
    assert lower_case(input_word) == expected_result, f"{input_word} com todas as letras minúsculas é igual a {expected_result}"

@pytest.mark.parametrize("input_word, expected_result", [
    ('gabriel', 'Gabriel'),
    ('davi', 'Davi'),
    ('python', 'Python'),
])
def test_capitalize(input_word, expected_result):
    assert capitalize(input_word) == expected_result, f"{input_word} com a primeira letra maiúscula é igual a {expected_result}"

@pytest.mark.parametrize("input_word, expected_result", [
    ('gabriel', 'leirbag'),
    ('davi', 'ivad'),
    ('python', 'nohtyp'),
])
def test_reverse(input_word, expected_result):
    assert reverse(input_word) == expected_result, f"{input_word} invertido é igual a {expected_result}"
