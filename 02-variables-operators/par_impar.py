n = 0


if n > 0:
  print("Is positive par" if n % 2 == 0 else "Is positive impar")
elif n < 0:
  print("Is negative par" if n % 2 == 0 else "Is negative impar")
else:
  print("The number is 0")