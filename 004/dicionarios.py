
gabriel = {
    'nome': 'Gabriel',
    'github': 'gabrielbdornas',
    'notas': [10,20,30],
}

romano = {
    'nome': 'romano',
    'github': 'halvesromano',
    'nota': [10,20,30],
}

isabelle = {
    'nome': 'isabelle',
    'github': 'Isabelle-Fernandes',
    'notas': [10,20,30],
}

usuarios = [gabriel, romano, isabelle]

for key in isabelle:
    print(f'O dicinário isabelle tem a chave {key} de valor {isabelle[key]}')
