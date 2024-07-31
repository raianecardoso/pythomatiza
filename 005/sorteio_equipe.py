import random

def sorteio():
    equipe = {
        1: 'André',
        2: 'Cora',
        3: 'Felipe',
        4: 'Gabriel',
        5: 'Henrique',
        6: 'Isabelle',
        7: 'Raiane',
        8: 'Romano',
        9: 'Yan',
    }
    sorteado = random.randrange(1, 10)
    return f'Foi sorteado o número {sorteado} e, portanto, o escolhido para organizar nosso próximo hh é {equipe[sorteado]}'
