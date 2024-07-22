# Um novo paciente chamado João deu entrada no hospital.
# Ele tem 20 anos e é um novo paciente deste hospital.
# Defina variáveis para armazenar o nome deste paciente,
# sua idade e se ele é um novo paciente da instituição.
# Mostre no sistema todas estas informações coletadas.

# nome
# paciente
# name
nome_paciente = input('Qual é o seu nome: ') # str
idade = input('Qual é a sua idade: ') #int
resposta_novo_paciente = input('Você já foi atendido neste hospital: (Sim ou Não): ')
novo_paciente = False

if resposta_novo_paciente.lower() == 'sim':
    novo_paciente = True

mensagem = 'o paciente ' + nome_paciente + ' de ' + str(idade) + ' anos'



if novo_paciente:
    print(mensagem, 'é um novo paciente')
else:
    print(mensagem, 'NÃO é um novo paciente')
