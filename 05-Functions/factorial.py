def factorial(n):
  print('Valor inicial', n)
  if n > 1:
    n = n * factorial(n - 1)
  print('Valor inicial', n)
  return n
n = int(input('Type number: '))
f = factorial(n)
print('Su factorial es: ', f)