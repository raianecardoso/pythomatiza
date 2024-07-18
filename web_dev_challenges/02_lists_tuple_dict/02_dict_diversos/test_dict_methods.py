from dict_methods import (
    find_dict_element,
    correct_dict,
    add_dict_item,
    find_out_key_error,
)
import inspect
import pytest

def test_not_none():
  assert find_dict_element() is not None, "Esperado valor diferente de 'None'"
  assert correct_dict() is not None, "Esperado valor diferente de 'None'"
  assert add_dict_item() is not None, "Esperado valor diferente de 'None'"
  assert find_out_key_error() is not None, "Esperado valor diferente de 'None'"

def test_type():
  assert type(find_dict_element()) == int, "Esperado um número inteiro"
  assert type(correct_dict()) == dict, "Esperado um dicionário"
  assert type(add_dict_item()) == dict, "Esperado um dicionário"
  assert type(find_out_key_error()) == int, "Esperado um número inteiro"

def test_parameters():
  assert len(inspect.getfullargspec(find_dict_element).args) == 0, "Assinatura da função não deverá receber parâmetros"
  assert len(inspect.getfullargspec(correct_dict).args) == 0, "Assinatura da função não deverá receber parâmetros"
  assert len(inspect.getfullargspec(add_dict_item).args) == 0, "Assinatura da função não deverá receber parâmetros"
  assert len(inspect.getfullargspec(find_out_key_error).args) == 0, "Assinatura da função não deverá receber parâmetros"

def test_find_dict_element():
  assert find_dict_element() == 8, f"Nota do aluno Júlio é 8"

def test_correct_dict():
  assert correct_dict() == {
                            'Júlio': 8,
                            'Antônio': 9,
                            'Maria': 7
                          }, f"Retorne o my_dict sem a aluna 'Ana'"
  with pytest.raises(Exception) as e_info:
    correct_dict()['Ana'], f"Retorne o my_dict sem a aluna 'Ana'"

def test_add_dict_item():
  assert add_dict_item()['Carla'] == 0, f"Nota do aluno Carla é 0"

def test_find_out_key_error():
  assert find_out_key_error() in [10, 8, 9, 7], f"Nota 10, 8, 9 e 7 esperadas"
