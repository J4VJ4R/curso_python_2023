from figures import Square, Circle, test_figure

def main():
  while True:
    menu = """
      GEOMETRICS FIGURES
      
      1-Square
      2-Circle
      3-Exit

      Choice the option: --> 
    """
    option = input(menu)
    if option == '1':
      base = float(input('Type base: '))
      height = float(input('Type height: '))
      square1 = Square('Square', base, height )
      test_figure(square1)
    elif option == '2':
      radius = float(input('Type radius: '))
      circle1 = Circle(radius)
      test_figure(circle1)
    elif option == '3':
      print('Programa closed...')
      exit()
    else:
      print('Option not found.. type again your option')
    

if __name__ == '__main__':
  main()