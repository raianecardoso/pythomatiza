def can_vote(age):
    # Melhorar função can_vote já implementada em 02-if/01-posso-votar/my_vote.py
    # TODO: Sendo informado a idade retorne a informação se a pessoa poderá votar seguindo as regras:
    # Menores de 0 anos = "Idade inexistente"
    # Menores de 16 anos = "Não pode votar"
    # Entre 16 e 17 anos = "Podem votar mas não são obrigados"
    # Entre 18 e 70 anos = "Obrigados a votar"
    # Maiores de 70 anos = "Podem votar mas não são obrigados"
    if age < 0:
        return 'Idade inexistente'
    if age >= 0 and age < 16:
        return 'Não pode votar'
    if age >=16 and age <=17:
        return 'Podem votar mas não são obrigados'
    if age >=18 and age <=70:
        return 'Obrigados a votar'
    if age > 70:
        return 'Podem votar mas não são obrigados'

def valid_password(password):
    # TODO: Verifique se a senha (password) é válida e retorne 'Válida' ou 'Não válida' conforme as regras:
    # Somente senhas com tamanho mínimo de 6 e máximo de 16 caracteres
    password_len = len(password)
    if password_len >= 6 and password_len <=16:
        return 'Válida'
    else:
        return 'Não válida'


def vowel_count(string):
    # TODO: Conte o número de vogais existentes na string passada como parâmetro.
    # Exemplo 1: string = 'Olá Mundo' return = 4
    # Exemplo 2: string = 'Sirius Education' return = 8
    vowels = ['a', 'á', 'e', 'é', 'ê', 'i', 'i', 'o', 'ô', 'ó', 'u', 'ú']
    count = 0
    for letter in string:
        if letter.lower() in vowels:
            count += 1
    return count
