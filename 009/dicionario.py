from pprint import pprint

dicionario = {
    'zueira': 'não sei',
    'casa': 'house',
    'cavalo': 'horse',
    'amor': 'love',
    'amor': 'love222',
    'amor': 'love2223',
}

pessoas = [
    {
        'id': 1,
        'nome': 'Gabriel',
        'idade': 39,
        'sexo': 'm',
        'profissão': 'eppgg',
        'signo': 'capricórnio',
    },
    {
        'id': 2,
        'nome': 'Cora',
        'idade': 22,
        'sexo': 'f',
        'profissão': 'eppgg',
        'signo': 'peixes',
    },
    {
        'id': 3,
        'nome': 'Henrique',
        'idade': 24,
        'sexo': 'm',
        'profissão': 'eppgg',
        'signo': 'cancer',
    },
]

for pessoa in pessoas:
    print(f"{pessoa['id']} - {pessoa['nome']}")

pessoas_gambi = [
    ['gabriel', 'cora', 'henrique'],
    [39, 22, 24],
    ['m', 'f', 'm']
]
