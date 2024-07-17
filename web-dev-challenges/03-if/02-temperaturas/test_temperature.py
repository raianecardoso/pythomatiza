from temperature import temp_converter
import inspect
import pytest

def test_not_none():
  assert temp_converter(18, 'celsius') is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(temp_converter(18, 'celsius')) == float or type(temp_converter(18, 'celsius')) == int, "Esperado valor numérico retorno da função"

def test_parameters():
  assert len(inspect.getfullargspec(temp_converter).args) == 2, "Assinatura da função poderá receber apenas dois parâmetros"

@pytest.mark.parametrize("temp, metric, expected_result", [
  (35, 'celsius', 95),
  (104, 'fahrenheit', 40),
])
def test_temp_converter(temp, metric, expected_result):
  assert temp_converter(temp, metric) == expected_result, f"{temp} graus {metric} convertido = {expected_result}"

