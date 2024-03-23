startnumber = int(input('Type number 1: '))
finalnumber = int(input('Type number 2: '))

positivenumbers = 0
neggativenumbers = 0

for number in range(startnumber, finalnumber):
  print(number)
  if number > 0:
    positivenumbers+=1
  elif number < 0:
    neggativenumbers+=1

print('='*30)
print(f'Positive numbers quantity = {positivenumbers}')
print(f'Neggative numbers quantity = {neggativenumbers}')
print('='*30)