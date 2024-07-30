from my_vote import can_vote
import inspect
import pytest

def test_not_none():
    assert can_vote(18) is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(can_vote(18)) == bool, "Esperado booleano como retorno da função"

def test_parameters():
    assert len(inspect.getfullargspec(can_vote).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"

@pytest.mark.parametrize("age, expected_result", [
  (18, True),
  (0, False),
  (17, False),
  (90, True),
  (25, True),
])
def test_can_vote(age, expected_result):
    answer = ''
    if expected_result == True:
        answer = 'Sim'
    else:
        answer = 'Não'
    assert can_vote(age) == expected_result, f"Pessoas com {age} podem votar? {answer}"
