
import random

def game(num, randomnum):
  
  
  if num == randomnum:
    print('You winnn!!!')
    print('End of the game...')
    exit()
  elif num > randomnum:
    print('The number is bigger, try again...')
  elif num < randomnum:
    print('The number is less, try again...')
    

def main():
  while True:
    print('='*30)
    print('---- Welcome to the game ----')
    print('---- Instructions: ----')
    print('---- Type any value to guess ----')
    print('---- the hidden number. ----')
    print('='*30)
    menu = """
    1. Easy
    2. Intermediate
    3. Hero
    4. Exit

    Choice the level... 
    """
    level = input(menu)
    lifes = 0
    #Lifes of the game
    if level == '1':
      lifes = 10 
    elif level == '2':  
      lifes = 7 
    elif level == '3':
      lifes = 5
    elif level == '4':
      print('Good bye :)...')
      exit()
    else:
      print('Some is bad in your type :(')
      print('Type again...')
    #Number random
    randomnum = random.randint(1, 10)
    while lifes <= lifes and lifes > 0: # I'm alive
      print('Remaining lifes: ', lifes)
      #Time for the user, to type a number
      num = int(input('Type a number: '))
      game(num, randomnum)
      lifes -= 1
    print('You lost!! bye :(')
if __name__ == '__main__':
  main()