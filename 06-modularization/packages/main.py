import my_package.aritmetic as a

def main():
  add  = a.add(1, 2, 3, 4)
  sub = a.sub(3, 4)
  exp = a.exp(2, 2)

  print('The add is: ', add)
  print('The sub is', sub)
  print('The exp is', exp)

if __name__ == '__main__':
  main()