from sys import argv

if len(argv) == 4:
  name = argv[1]
  age = int(argv[2])
  height = float(argv[3])

  print(f'Name: {name} \nAge: {age} \nHeigh: {height}')
else:
  print('Was an error, verify your data')
  print('Example: format.py "Name" 25 1.67 ')