import math
print('-------- CIRCLE AREA --------')

def calculate_circle_are(radius):
  return math.pi * radius**2

radius = 5 #Example radius
area = calculate_circle_are(radius)
area = round(area, 2)
print("The area is: ", area)