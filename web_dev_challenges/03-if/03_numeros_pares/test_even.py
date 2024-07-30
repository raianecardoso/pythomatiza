from even import is_even
import inspect
import pytest

def test_not_none():
    assert is_even(18) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(is_even(18)) == str, "Esperado string no retorno da função"

def test_parameters():
    assert len(inspect.getfullargspec(is_even).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"

@pytest.mark.parametrize("number, expected_result", [
  (2, 'Número é par'),
  (3, 'Número é inpar'),
  (20, 'Número é par'),
])
def test_is_even(number, expected_result):
    assert is_even(number) == expected_result, f"{expected_result}: {number}"
