class Person:

  #constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age
  #Methods
  #Show data
  def show_data(self):
    print('Name: ', self.name)
    print('Age: ', self.age)

  def __str__(self):
    return f'Name: {self.name} \nAge: {self.age}'