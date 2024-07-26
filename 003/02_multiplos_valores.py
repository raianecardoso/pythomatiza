x, y, z = 'Laranja', 'Banana', 'Maçã'
print(x, y, z)

a = b = c = 'Uva'
print(a, b, c)

# unpack

frutas = ['Abacaxi', 'Melão', 'Pera']
d, e, f = frutas
print(d, e, f)

g, h, i = 'Uva'
print(g, h, i)

nome = 'Gabriel'
print(nome)

def ola_mundo():
    return 'Olá mundo'

resultado_func = ola_mundo()
print(resultado_func)
print(ola_mundo())


def soma(a, b):
    return a + b

resultado_soma = soma(568, 987)
print(resultado_soma)
