from calculator import calculator
import inspect
import pytest
from unittest import mock

@mock.patch("calculator.input")
def test_not_none(mock_input):
    mock_input.return_value = 3
    assert calculator() is not None, "Esperado valor diferente de 'None'"

@mock.patch("calculator.input")
def test_type(mock_input):
    mock_input.return_value = 3
    assert type(calculator()) == int or type(calculator()) == float, "Esperado valor numérico (int ou float)"

def test_parameters():
    assert len(inspect.getfullargspec(calculator).args) == 0, "Assinatura da função não pode receber nenhum parâmetros"

@pytest.mark.parametrize("number, expected_result", [
    (3, 6),
    (6, 12),
    (1, 2),
    (7, 14),
])
@mock.patch("calculator.input")
def test_calculator(mock_input, number, expected_result):
    mock_input.return_value = number
    assert calculator() == expected_result, f"{number} + {number} = {expected_result}"
