import random
from typing import List, Dict
def greats()->str:
  """
  Return a random great with name givving
  Return:
    str: Random greates with correct format
  """
  greats = [
    "Hi {} is good see you egein",
    "Hi {} is perfect, you again!!",
    "Hi {} welcome!!",
  ]
  return random.choice(greats)

def hi(name:str)->str:
  """
  Generete a personalized greate
  Args:
    name (str): Name of the user
  Return:
    Personalized greate (str)
  """
  if name == "":
    print("The name is empty, try again")
  great = greats().format(name)
  return great


def holas(names:List)->Dict:
  """
  Generete a personalized greate list
  Args:
    names (list[str]): Names of the users
  Return:
    Dict[str, str]: Dictionary with the greates with key and value
  """
  greatslist = {}
  for name in names:
    greatsnew = hi(name)
    greatslist[name] = greatsnew
    
  return greatslist
  
listname = ["Alex", "Baron", "Camila"] 
