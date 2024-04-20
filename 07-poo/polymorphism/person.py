class Person(object):
  def __init__(self, name):
    self.name = name

  def movement(self):
    print('I am walking')
  
class Athlete(Person):
  def movement(self):
    print('I am running')

class Rider(Person):
  def movement(self):
    print('I am riding')