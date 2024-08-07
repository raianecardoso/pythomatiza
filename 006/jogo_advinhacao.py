import random

def adivinha():
    numero = random.randint(0,100)
    valor = int(input('digite um numero: '))
    while(valor != numero):
        if valor < numero:
            valor = int(input('Valor MENOR que o numero. Digite novamente: '))
        else:
            valor = int(input('Valor MAIOR que o numero. Digite novamente: '))
    print('Parabéns, você acertou!')


adivinha()
