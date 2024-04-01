list = []

largest = 0
smallest = 0

print('='*30)
print('---------- TYPE SIX NUMBERS ----------')

#Type numbers
n1 = int(input('Type number 1: '))
list.append(n1)
n2 = int(input('Type number 2: '))
list.append(n2)
n3 = int(input('Type number 3: '))
list.append(n3)
n4 = int(input('Type number 4: '))
list.append(n4)
n5 = int(input('Type number 5: '))
list.append(n5)
n6 = int(input('Type number 6: '))
list.append(n6)

#Functions to largest and smallest number
largest = max(list)
smallest = min(list)
print('='*30)
print(f'The largest number is: {largest}')
print('='*30)
print(f'The smallest number is: {smallest}')
print('='*30)