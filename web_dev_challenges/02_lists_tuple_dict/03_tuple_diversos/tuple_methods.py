def tuple_sum():
    # TODO: Calcule a soma dos elementos da  tupla 'my_tuple'
    my_tuple = 1, 2, 3, 4, 5
    soma = 0
    for i in range(len(my_tuple)):
        soma += my_tuple[i]
    return soma

def find_second_element():
    # TODO: Retorne o segundo elemento da tupla 'my_tuple'
    my_tuple = 1, 2, 3, 4, 5
    return my_tuple[1]

def find_out_typle_error():
    # TODO: Encontrar o erro no código abaixo
    # TODO: my_tuple não deverá ser modificada
    my_tuple = 1, 2, 3, 4, 5
    # i = list(my_tuple)
    # i.remove(1)
    # my_tuple = tuple(i)
    return my_tuple
