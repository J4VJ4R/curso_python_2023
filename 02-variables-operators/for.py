product_list = []
counter = 0
while True:
  product = input("Type your product: ")
  if product == "Done":
    break
  product_list.append(product)
  counter += 1

for index, value in enumerate(product_list, start = 1 ):
  print(f"Product {index} {value}")

product_list = []


