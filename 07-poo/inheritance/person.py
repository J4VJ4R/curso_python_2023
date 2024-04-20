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

#Class customer inheritance from person

class Employee(Person):
  def __init__(self, name, age, salary):
    super().__init__(name, age)
    self.salary = salary

  def detail_customer(self):
    super().details_person()
    print('Salary:', self.salary)

  def __str__(self):
    return super().__str__() + f'\nSalary: {self.salary}'