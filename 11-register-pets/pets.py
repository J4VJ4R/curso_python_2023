class Animal:
  def __init__(self, type, age) -> None:
    self.age = age
    self.type = type

  def __str__(self) -> str:
    return f"Animal[The {self.type} is {self.age}]"

class Pet(Animal):
  def __init__(self, type, age, name) -> None:
    super().__init__(type, age)
    self.name = name
  
  def info(self):
    print(f"The {self.type} is {self.age} her name is {self.name}")

pet1 = Pet("Dog", "1 Year", "Moon")
pet1.info()