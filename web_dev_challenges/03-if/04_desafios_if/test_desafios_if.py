from desafios_if import (
                  can_vote,
                  valid_password,
                  vowel_count,
                  )
import inspect
import pytest

def test_not_none():
  assert can_vote(18) is not None, "Esperado valor diferente de 'None'"
  assert valid_password('1234') is not None, "Esperado valor diferente de 'None'"
  assert vowel_count('Olá Mundo') is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(can_vote(18)) == str, "Esperado string no retorno da função"
  assert type(valid_password('1234')) == str, "Esperado string no retorno da função"
  assert type(vowel_count('Olá Mundo')) == int, "Esperado número inteiro no retorno da função"

def test_parameters():
  assert len(inspect.getfullargspec(can_vote).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"
  assert len(inspect.getfullargspec(valid_password).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"
  assert len(inspect.getfullargspec(vowel_count).args) == 1, "Assinatura da função poderá receber apenas um parâmetro"

@pytest.mark.parametrize("age, expected_result", [
  (-1, "Idade inexistente"),
  (0, "Não pode votar"),
  (14, "Não pode votar"),
  (16, "Podem votar mas não são obrigados"),
  (17, "Podem votar mas não são obrigados"),
  (18, "Obrigados a votar"),
  (70, "Obrigados a votar"),
  (71, "Podem votar mas não são obrigados"),
  (90, "Podem votar mas não são obrigados"),
])
def test_can_vote(age, expected_result):
  assert can_vote(age) == expected_result, f"Pessoas com {age}: {expected_result}"

@pytest.mark.parametrize("password, expected_result", [
  ('123456', 'Válida'),
  ('1234567a', 'Válida'),
  ('12345', 'Não válida'),
  ('1236789112345', 'Válida'),
  ('12367891123456769', 'Não válida'),
  ('Sirius Education', 'Válida'),
])
def test_valid_password(password, expected_result):
  assert valid_password(password) == expected_result, f"Senha {password} {expected_result}"

@pytest.mark.parametrize("string, expected_result", [
  ('Ola Mundo', 4),
  ('Sirius Education', 8),
])
def test_vowel_count(string, expected_result):
  assert vowel_count(string) == expected_result, f"String {string} possui {expected_result} vogais"
