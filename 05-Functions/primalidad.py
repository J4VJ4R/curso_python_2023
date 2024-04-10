#Prime number
def primeNum(num):
  contador = 0
  
  for i in range(1, num + 1):
    if i == 1 or i == num:
      continue

    if num % i == 0:
      contador += 1

  if contador == 0:
    return True
  else:
    return False

#Funciń principal
def main():
  number = int(input("Type a number --> "))
  result = primeNum(number)

  if result:
    print('Is prime number')
  else:
    print('Isn\'t prime number')


#Punto de entrada de la aplicación
if __name__ == '__main__':
  main()