from desafios_essencial import (
    mega_combinations,
    word_len,
    full_name,
    is_even,
    calculator,
)
import pytest


def test_mega_combinations():
  assert mega_combinations() == 50063860, "Esperado valor exato de combinações de 6 números em 60"

def test_mega_combinations_type():
  assert type(mega_combinations()) == int, "Esperado número inteiro"

@pytest.mark.parametrize("first_name, last_name, expected_result", [
  ('gabriel', 'dornas', 'Gabriel Dornas'),
  ('Maria', 'José', 'Maria José'),
  ('JOSÉ', 'MARIA','José Maria'),
])
def test_full_name(first_name, last_name, expected_result):
  assert full_name(first_name, last_name) == expected_result, f"{first_name} e {last_name} gera o nomer completo {expected_result}"

@pytest.mark.parametrize("number, expected_result", [
  (2, True),
  (3, False),
  (20, True),
])
def test_is_even(number, expected_result):
  assert is_even(number) == expected_result, f"{number} é par: {expected_result}"

@pytest.mark.parametrize("word, expected_result", [
  ('soma', 4),
  ('multiplicação', 13),
  ('subtração', 9),
  ('divisão', 7),
  ('módulo', 6),
])
def test_word_len(word, expected_result):
  assert word_len(word) == expected_result, f"A string {word} tem {expected_result} caracteres"

@pytest.mark.parametrize("first_number, second_number, operation, expected_result", [
  (2, 3, 'soma', 5),
  (2, 7, 'multiplicação', 14),
  (5, 1, 'subtração', 4),
  (5, 1, 'divisão', 5),
  (5, 1, 'módulo', 0),
])
def test_calculator(first_number, second_number, operation, expected_result):
  assert calculator(first_number, second_number, operation) == expected_result, f"{operation} de {first_number} e {second_number} = {expected_result}"
