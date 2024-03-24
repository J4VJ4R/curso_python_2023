#Title
print('='*30)
print('-------- COFFEE SHOP ---------')
print('='*30)

#Variables
gratuity10 = 0
gratuity20 = 0
gratuity30 = 0
totalgratuity = 0

#Data to type
valuesale = float(input('Price of sale: '))

#Condition to gratuity
if valuesale <= 100:
    gratuity10 = valuesale * 0.10
    totalgratuity = gratuity10
elif valuesale > 100 and valuesale < 200:    
  gratuity20 = valuesale * 0.20
  totalgratuity = gratuity20
elif valuesale > 200:    
  gratuity30 = valuesale * 0.30
  totalgratuity = gratuity30

totaltaxes = valuesale * 0.19
fulltotal = valuesale + totaltaxes - totalgratuity

print(f'GRATUITY = $', totalgratuity)
print(f'TAX = $', totaltaxes)
print(f'TOTAL = $', fulltotal)