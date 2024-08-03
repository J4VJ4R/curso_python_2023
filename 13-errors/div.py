try:
  n1 = int(input("Type your number 1: "))
  n2 = int(input("Type your number 2 different to 0: "))

  result = n1 / n2
except ValueError:
  print("Error, imposible devision by letters")
except ZeroDivisionError:
  print("Error, imposible devision by 0")
except Exception as e:
  print("Error", e)
else:
  print(f"División of {n1} / {n2} = {result}")

  