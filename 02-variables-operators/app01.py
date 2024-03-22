print('='*30)
print('--------- TYPE NUMBER ---------')
print('='*30)

num1 = input('--> ')
num1 = int(num1)
if(num1 % 2 == 0 and num1 > 0):
  print('The number is positive even')
elif(num1 % 2 == 0 and num1 < 0):
  print('The number is negative even')
elif(num1 % 2 != 0 and num1 > 0):
  print('The number is positive odd')
elif(num1 % 2 != 0 and num1 < 0):
  print('The number is negative odd')
else:
  print('The number is neutral')   
