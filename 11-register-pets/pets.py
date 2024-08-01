class Animal:
  def __init__(self, age, type) -> None:
    self.age = age
    self.type = type

Animal1 = Animal("4 meses", "Perro")
Animal2 = Animal("1 año", "Gato")


print(Animal1.type)
print(Animal2.type)