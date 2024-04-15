import sys

if len(sys.argv) == 3:
  text = sys.argv[1]
  qty = int(sys.argv[2])

  counter = 0
  while counter < qty:
    print(text)
    counter+=1
else:
  print('Was an error, verify your data')
  print('Example: in_script.py "Test" 5 ')