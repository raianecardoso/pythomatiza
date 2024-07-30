def days_in_a_month(month):
  # TODO: Informado o mês desejado, retornar o número de dias
  # TODO: Fevereiro será considerado como 28 dias
  # Auxílio: Utilize um dicionário para facilitar o trabalho
  meses_dias = {
    "Janeiro": 31,
    "Fevereiro": 28,
    "Março": 31,
    "Abril": 30,
    "Maio": 31,
    "Junho": 30,
    "Julho": 31,
    "Agosto": 31,
    "Setembro": 30,
    "Outubro": 31,
    "Novembro": 30,
    "Dezembro": 31
}
  return meses_dias[month]

def calory_counter(first_item, second_item, third_item):
  # TODO: Contar quantas calorias em seu pedido na lanchonete
  # TODO: Dado o dicionário my_foods, retorne a soma das calorias dos três itens solicitados
  my_foods = {
    "Hamburger": 250,
    "Cheese Burger": 300,
    "Cheese Bacon Egg": 540,
    "Cheese Bacon Chicken": 350,
    "French Fries": 230,
    "Salad": 15,
    "Coca Cola": 150,
    "Sprite": 150,
    }
  return my_foods[first_item] + my_foods[second_item] + my_foods[third_item]
