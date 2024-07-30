minha_primeira_list = []
colegas = ['Romano', 'Henrique', 'Isabelle', 'Cora', 'Raiane']
numeros = [1,2,3,4,5,6,7,8,9]

for colega in colegas:
    print(colega.upper())

for numero in numeros:
    par = numero % 2
    if par == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} NÃO é par!')

