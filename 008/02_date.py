from datetime import datetime, timedelta

# data = datetime.strptime('07/08/2024', '%d/%m/%Y')
data = datetime.now()
nova_data = data + timedelta(days=7)

print(f'Hojé é dia {data.day}, semana que vem será dia {nova_data.day}!')
