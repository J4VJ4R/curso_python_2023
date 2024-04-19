class Person:
  __name = None
  __age = None

  def __init__(self, name, age):
    self.__name = name
    self.__age = age
  
  def __method_private(self):
    print('I am private')

  def get_name(self):
    return self.__name

  def set_name(self, name):
    self.__name = name

  def get_age(self):
    return self.__age
  
  def set_age(self, age):
    self.__age = age
  
  def __str__(self):
    return f'Name: {self.__name} \nAge: {self.__age}'