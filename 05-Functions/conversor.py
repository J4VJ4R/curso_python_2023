

def conversor(value, country):
  # 1 = Colombia COP
  # 2 = Mexico MXN
  if country == 1:
    dollar_value = 3828
    total = 0

    if value and value > 0:
      total = value * dollar_value
    else:
      print('Incorrect value')

    return total
  elif country == 2:
    dollar_value = 16.64
    total = 0

    if value and value > 0:
      total = value * dollar_value
    else:
      print('Incorrect value')

    return total
  


def main():
  while True:
    menu = """
    Choice the country: 
    1. Colombia: 
    2. México: 
    3. Exit: 
    """
    country = input(menu)
    if country == '1':
      value = float(input('Type COP value: '))
      total_cop = conversor(value, country)
      print(total_cop, 'Colombian pesos')
    elif country == '2':
      value = float(input('Type MXN value: '))
      total_cop = conversor(value, country)
      print(total_cop, 'Mexican pesos')
    elif country == '3':
      print('Application clossing....')
      exit()
    else:
      print('Wrong option ;x')
      print("Type egain your option.")

if __name__ == '__main__':
  main()