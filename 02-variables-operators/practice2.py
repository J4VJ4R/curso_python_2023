# Calculate sale price

print('----- STORE COFFEE -----')
item1 = input('Type price 1: ')
item2 = input('Type price 2: ')

item1 = float(item1)
item2 = float(item2)

price = item1 + item2
taxes = price * 0.18
totalprice = price + taxes
print('='*30)
print('Price without taxes: ', price)
print('Taxes: ', taxes)
print('Price with taxes: ', totalprice)
print('='*30)