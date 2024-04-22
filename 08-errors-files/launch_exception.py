class ExceptionOperator(Exception):
  def __init__(self, message):
    super().__init__(message)
def div(a, b):
  if b == 0:
    raise ExceptionOperator('Error: No is posible division with cero')
div(4, 0)