product = ""
product_list = []
counter = 0
index = 0
while product != "Done":
  product = input("Type your product: ")
  product_list.append(product)
  counter += 1

for item in product_list:
  print(f"Product {index} {item}")
  index += 1

product_list = []


