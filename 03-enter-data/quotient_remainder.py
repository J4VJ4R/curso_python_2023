print("Enter the number for console")

# Data for console
a = input("Number 1: ")
b = input("Number 2: ")

# Change to int
a = int(a)
b = int(b)

quotient = a // b
remainder = a % b

print(f'Quotient: {quotient} \nRemainder: {remainder}')