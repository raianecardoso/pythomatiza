Pythomatiza
===

![test status](../coverage-badge/tests.svg?raw=true)

## Setup projeto

- Fork o repositório para seu usuário github. Não se esqueça de desmarcar a opção "Copy the `main` branch only" antes de clicar em `Create fork`.

![image](https://github.com/user-attachments/assets/c5f08479-32ab-4815-b41a-f157c5483912)

![image](https://github.com/user-attachments/assets/ead55832-c990-46ab-a312-c49c308f1a6e)

- Autorize o funcionamento dos Actions:

- Clone o repositório forkado e instale os pacotes:

```python
# clonar o repositório forkado (repositório criado em seu usuário e não o da organização automatiza-mg)
git clone git@github.com:<usuario-github>/pythomatiza.git

# navegar para o repositório criado
cd pythomatiza

# criar remote upstream
# caminho abaixo usa ssh
git remote add upstream git@github.com:automatiza-mg/pythomatiza.git

# criar ambiente virtual python e instale os pacotes necessários - Windows
$ python -m venv venv
$ . venv/Scripts/activate
$ pip install -r requirements.txt

# criar ambiente virtual python e instale os pacotes necessários - Linux e Mac
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

## Como realizar o onboarding dos para realizar exercícios

```python
# navegar para o nosso repositório
# não copie o código abaixo cegamente
$ cd ~/caminho/para/pythomatiza

# ativar ambiente virtual python
# windows
$ . venv/Scripts/activate
# linux e mac
$ . venv/bin/activate

# certificar que não há nada para commitar
# se git status não estiver limpo, commit/restore
$ git status

# certificar que você está com a versão mais atualizada
# git pull upstream main -X ours
$ task up
```

## Como rodar seus testes

```python
# navegar até a pasta do desafio/exercício desejado
# não copie o código abaixo cegamente
$ cd ~/caminho/para/pythomatiza/web-dev-challenges/pasta/desafio/desejado

# abrir o desafio no editor de texto para resolvê-lo
# commitar quando achar necessário

# rodar os testes
$ pytest
```
