head = 0
quee = 0
med = 0
n1 = int(input('Type number 1: '))
n2 = int(input('Type number 2: '))
n3 = int(input('Type number 3: '))

if n1 > n2 and n1 > n3:
  head = n1
elif n2 > n1 and n2 > n3:
  head = n2
else:
  head = n3

if n1 < n2 and n1 < n3:
  quee = n1
elif n2 < n1 and n2 < n3:
  quee = n2
else:
  quee = n3
  
if (n2 < n1 and n2 > n3) or (n2 > n3 and n2 < n3) :
  med = n2
elif (n3 < n2 and n3 > n1) or (n3 < n1 and n3 > n1):
  med = n3
elif (n1 < n2 and n1 > n3) or (n1 > n2 and n1 < n3):
  med = n1 


print('='*30)
print(f'Mayor: {head}')
print(f'Intermediate: {med}')
print(f'Menor: {quee}')
print('='*30)
