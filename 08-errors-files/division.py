div = 0
try:
  a = int(input('Type number 1: '))
  b = int(input('Type number 2: '))

  div = a / b
except ZeroDivisionError:
  print('Error, the division can\'t with cero')
except ValueError:
  print('Error. Type only numbers')
except Exception as error:
  print('Was an error: ', type(error).__name__)
print(div)