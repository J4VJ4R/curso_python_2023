import random
pairs = []
odd = []
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for value in tuple1:
  rannumber = random.randint(1, 100)
  value2 = value * rannumber
  print(f'{value} * {rannumber} = {value2}')
  if(value2 % 2 == 0):
    pairs.append(value2)
  else:
    odd.append(value2)
print(pairs)
print(odd)
