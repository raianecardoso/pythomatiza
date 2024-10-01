import math

def mega_combinations():
    # Para pratirar a utilização de bibliotecas externas.
    # TODO:  calcule o número inteiro de combinações possíveis para um jogo da mega sena
    # Auxílio: https://www.w3schools.com/python/ref_math_comb.asp
    return(math.comb(60,6))

def word_len(word):
    # Para pratirar a utilização de métodos já disponíveis
    # TODO: Retorne um número inteiro do número de caracteres de uma palavra (word)
    # Auxlílio: https://www.w3schools.com/python/ref_func_len.asp
    return int(len(word))

def full_name(first_name, last_name):
    # Para pratirar a utilização de métodos já disponíveis e concatenação de strings
    # TODO: Retorne uma string única com o nome completo.
    # TODO: A string retorna deve contar a primeira letra dos dois nomes maiúscula
    # Exemplo 1: frist_name = 'gabriel', last_name = 'dornas', resultado = 'Gabriel Dornas'
    # Exemplo 2: frist_name = 'Maria', last_name = 'José', resultado = 'Maria José'
    # Exemplo 3: frist_name = 'JOSÉ', last_name = 'MARIA', resultado = 'JOSÉ MARIA'
    # Auxílio: https://www.w3schools.com/python/python_strings_methods.asp
    return first_name.capitalize() +' '+ last_name.capitalize()

def is_even(number):
    # Para praticar pesquisas na internet
    # TODO: Retorne True se number for par e False se number for impar
    # Exemplo 1: number = 2,  resultado = True
    # Exemplo 2: number = 3,  resultado = False
    if number % 2 == 0:
        return True
    else:
        return False

def calculator(first_number, second_number, operation):
    # Desafio avançado. Necessário utilizar conhecimentos não demostrados ainda (condicionais)
    # Não se intimide. Faça uma busca na internet para tentar resolver a questão
    # TODO: Recebendo dois números e a operação desejada, deverá retornar valor calculado
    # Exemplo 1: first_number = 2, second_number = 3, operation = 'soma', resultado = 3
    # Exemplo 2: first_number = 2, second_number = 7, operation = 'multiplicação', resultado = 14
    # Exemplo 3: first_number = 5, second_number = 1, operation = 'subtração', resultado = 4
    # Exemplo 4: first_number = 5, second_number = 1, operation = 'divisão', resultado = 5
    # Auxílio:
    # se operation = 'soma', return first_number + second_number
    # se operation = 'multiplicação', return first_number * second_number
    # se operation = 'subtração', return first_number - second_number
    # se operation = 'divisão', return first_number / second_number
    # se operation for diferente das opções acima, return 0
    if operation == 'soma':
        return first_number + second_number
    elif operation == 'multiplicação':
        return first_number * second_number
    elif operation == 'subtração':
        return first_number - second_number
    elif operation == 'divisão':
        return first_number / second_number
    else:
        return 0
