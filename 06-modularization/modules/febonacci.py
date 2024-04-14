# module for fibonacci
def fibo(n):
  a, b = 0, 1
  while a < n:
    print(a, end=' ')
    a, b = b, a + b
    #1, 1, 2, 3, 5, 8 ...
  print()

def fibo2(n):
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, a + b
  return result