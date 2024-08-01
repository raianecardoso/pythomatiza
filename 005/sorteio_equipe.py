import random

def sorteio():
    equipe = [
        'André',
        'Cora',
        'Felipe',
        'Gabriel',
        'Henrique',
        'Isabelle',
        'Raiane',
        'Romano',
        'Yan',
    ]
    sorteado = random.choice(equipe)
    return f'O escolhido para organizar nosso próximo hh é {sorteado}'
