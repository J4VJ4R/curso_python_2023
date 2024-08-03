class Animal:
  """Animal principal Class for create other animals """
  def __init__(self, type, age) -> None:
    self.age = age
    self.type = type

  def __str__(self) -> str:
    return f"Animal[The {self.type} is {self.age}]"

class Pet(Animal):
  """Pet Class where inheritance from Animal"""
  def __init__(self, type, age, name) -> None:
    super().__init__(type, age)
    self.name = name

  def __str__(self) -> str:
    return f"Animal[The {self.type} is {self.age} her name is {self.name}]"
  
class RegisterPets():
  """Class for register pets"""
  def __init__(self) -> None:
    self.pets = []

  def addPet(self, pet):
    """
    Add a pet in the list

    Parameters:
      pet (Pet): The pet will add to register
    """
    self.pets.append(pet)  

  def listPets(self):
    """
    List all pets registered
    """
    if self.pets:
      print(" List about pets.\n ", "*"*30)
      for index, pet in enumerate(self.pets, start=1):
        print(f"{index} {pet}")
    else:
      print("No Any pets register")

  def editPet(self, index, new_pet):
    """
    Set pets
    Parameters:
      Index (int): Pet's index to edit
      new_pet (Pet): Pet's new information
    """
    if index < 0 or index >= len(self.pets):
      print("No any register pets here")
    else:
      print("The pet was updated")
      self.pets[index] = new_pet
      

  def deletePet(self, index):
    if index < 0 or index >= len(self.pets):
      print("No any register pets here")
    else:
      del self.pets[index]
      print("The pet was deleted")