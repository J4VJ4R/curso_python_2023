class Animal:
  def __init__(self, age, type) -> None:
    self.age = age
    self.type = type

  def info(self):
    print(f"The {self.type} is {self.age}")

Animal1 = Animal("4 months", "Dog")
Animal2 = Animal("1 year", "Cat")


Animal1.info()
Animal2.info()