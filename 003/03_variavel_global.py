nome = 'Gabriel'

def ola_pessoa():
    nome = 'Isabelle'
    return f'Olá {nome}'

print(nome)
print(ola_pessoa())
print(nome)

ola_python1 = 'Teste pergunta romano'

def ola_python():
    return 'Outro teste romano'

print(ola_python1)
print(ola_python)
print(ola_python())

def test_variavel_global():
    global novo_nome
    novo_nome = 'Henrique'
    return f'Olá {novo_nome}'

print(test_variavel_global())
print(novo_nome)
print(((2+2)/(5*6)))
