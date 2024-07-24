Python 18Horas
===

![test status](https://raw.githubusercontent.com/gabrielbdornas/python-18horas/coverage-badge/tests.svg?raw=true)

## Setup projeto

```python
# fork o repositório para seu usuário github
# clonar repositório forkado
git clone git@github.com:<usuario-github>/python-18horas.git

# navegar para o repositório criado
cd python-18horas

# criar remote upstream
# caminho abaixo usa ssh
git remote add upstream git@github.com:gabrielbdornas/python-18horas.git

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
$ cd ~/caminho/para/python-18horas

# certificar que não há nada para commitar
# se git status não estiver limpo, commit/restore
$ git status

# Certificar que você está com a versão mais atualizada
$ git pull upstream main -X ours
```

## Como rodar seus testes

```python
# navegar até a pasta do desafio/exercício desejado
# não copie o código abaixo cegamente
$ cd ~/caminho/para/python-18horas/web-dev-challenges/pasta/desafio/desejado

# abrir o desafio no editor de texto para resolvê-lo
# commitar quando achar necessário

# rodar os testes
$ pytest
```

