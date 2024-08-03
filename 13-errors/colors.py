class ColorValidation(Exception):
  def __init__(self, colour) -> None:
    super().__init__(f"The colour {colour} wasn't find")

def colors(colour):
  colors = ["blue", "red", "white"]
  if colour not in colors:
    raise ColorValidation(colour)

try:  
  colors("red")
except Exception as error:
  print("Error: ", error)

