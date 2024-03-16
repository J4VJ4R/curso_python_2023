a = input('Type first number: ')
b = input('Type second number: ')

a = float(a)
b = float(b)
quotient = a / b
res = a % b

quotient = round(quotient, 2)
res = round(res, 2)
print('Quotient = ', quotient)
print('Res = ', res)