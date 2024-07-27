product = ""
product_list = []
counter = 0
index = 0
while product != "Done":
  product = input("Type your product: ")
  product_list.append(product)
  counter += 1

while index < len(product_list):
  print(f"Producto {index}: {product_list[index]}")
  index += 1

product_list = []

