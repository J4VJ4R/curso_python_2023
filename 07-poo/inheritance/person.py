class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def details_person(self):
    print(f'Name: {self.name} \nAge: {self.age}')

  def __str__(self):
    return f'Name: {self.name} \nAge: {self.age}'

class Client(Person):
  pass