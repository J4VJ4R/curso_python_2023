product = ""
product_list = []
counter = 0
while product != "Done":
  product = input("Type your product: ")
  product_list.append(product)
  counter += 1

for index, value in enumerate(product_list, start = 1 ):
  print(f"Product {index} {value}")

product_list = []


