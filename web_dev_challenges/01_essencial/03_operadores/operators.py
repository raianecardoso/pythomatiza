def add(first_number, second_number):
  # TODO: retorne a soma dos parâmetros first_number e second_number
  return first_number + second_number

def sub(first_number, second_number):
  # TODO: retorne a subtração dos parâmetros first_number e second_number
  return first_number - second_number

def mult(first_number, second_number):
  # TODO: retorne a multiplicação dos parâmetros first_number e second_number
  return first_number * second_number

def div(first_number, second_number):
  # TODO: retorne a divisão dos parâmetros first_number e second_number
  return first_number / second_number

def expo(first_number, second_number):
  # TODO: retorne a exponenciação dos parâmetros first_number e second_number
  return first_number ** second_number

def remai(first_number, second_number):
  # TODO: retorne o resto da divisão dos parâmetros first_number e second_number
  return first_number % second_number

def quoti_remai(first_number, second_number):
  # TODO: retorne o quociente e o resto da divisão, nesta exata ordem, dos parâmetros first_number e second_number
  # Hint: Utilize a vírgula para separar os dois valores retornados na função
  quoti = first_number // second_number
  rem = remai(first_number, second_number)
  return quoti, rem
