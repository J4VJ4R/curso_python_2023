import math
#Main Class to figures
class Figure:
  def __init__(self, name):
    self.name = name
  def area():
    pass
  def perimeter():
    pass
#Class square where it inheritance from figure
class Square(Figure):
  #Constructor
  def __init__(self, name, base, height):
    super().__init__(name)
    self.base = base
    self.height = height
  #Function to obtain area
  def area(self):
    area = self.base * self.height
    return f'The area is: {area}'
  #Function to obtaein perimeter
  def perimeter(self):
    perimeter = self.height * 4
    return f'The perimeter is: {perimeter}'
  #Show figure data
  def __str__(self):
    return f'Details of Square: [Base: {self.base} Perimeter: {self.height}]'

#Class circle where it inheritance from figure
class Circle(Figure):
  pi = math.pi 
  def __init__(self, radius):
    self.name = __class__.__name__
    self.radius = radius
  #Function to obtain area of a circle
  def area(self):
    pi = math.pi
    area = pi * self.radius**2
    return f'The area of circle is: {round(area, 2)}'
  #Function to obtain perimeter of a circle
  def perimeter(self):
    pi = math.pi
    perimeter = 2*pi*self.radius
    return f'The perimeter of circle is: {round(perimeter, 2)}'
  #Show figure data
  def __str__(self):
    return f'Details of Square: [Area: {self.radius}]'

#Function to test figure
def test_figure(figure):
  print(figure)
  print('Area: ', figure.area())
  print('Perimeter: ', figure.perimeter())