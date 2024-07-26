"""
In this app we will build a software to calculate IVA
"""

value_product = input("Type product value:")

value_product = int(value_product)
iva = value_product * 18 / 100
final_value = iva + value_product

print("Value without iva is: ", value_product)
print("Value with iva is: ", final_value)
