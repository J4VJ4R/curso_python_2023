c = 0
add = 0

while c < 3:
  try:
    n = int(input(f'Type a number {c+1}: '))
    add += n
    c += 1
  except:
    print('Error: Only integer number...')
  else:
    print('All ok')
  finally:
    print('Programa closed')

print(f'The add is: {add}')