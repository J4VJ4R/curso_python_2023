print("Welcome to the blue store")
print("Do sales")
# Variables
price = 0
tax = 19
# Enter de product
print("""
  Chooce a product\n
      Rice 1\n
      Bread 2\n
      Apple 3\n
""")
      
code_product = input("Enter product code: ")
code_product = int(code_product)
if(code_product == 1):
    price = 2500
if(code_product == 2):
    price = 3000

# price for tax
price_tax = (price * 19) / 100

# final price
final_price = price_tax + price
print("="*25)
print("--- SALES BILL ---")
print("="*25)
print("Price without taxes = ", price)
print(f'Total price with taxes: {final_price}')
print("="*25)


