import random
from typing import List, Dict
def greats()->str:
  greats = [
    "Hi {} is good see you egein",
    "Hi {} is perfect, you again!!",
    "Hi {} welcome!!",
  ]
  return random.choice(greats)

def hi(name:str)->str:
  if name == "":
    print("The name is empty, try again")
  great = greats().format(name)
  return great


def holas(names:List)->Dict:
  greatslist = {}
  for name in names:
    greatsnew = hi(name)
    greatslist[name] = greatsnew
    
  return greatslist
  
listname = ["Alex", "Baron", "Camila"] 
