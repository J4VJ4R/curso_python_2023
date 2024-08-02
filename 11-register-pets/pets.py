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

  def __str__(self) -> str:
    return f"Animal[The {self.type} is {self.age} her name is {self.name}]"
  
  def speak(self):
    pass

class Dog(Pet):
  def speak(self):
    return "Woof!"
  
class Cat(Pet):
  def speak(self):
    return "Miau"
  
d = Dog("Dog", "1 year", "Waldo")
c = Cat("Dog", "2 year", "Ana")

print(d.speak())
print(c.speak())