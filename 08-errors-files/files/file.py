from io import open
from os import path

def write_file():
  file = open('./08-errors-files/files/text.txt', 'w')
  file.write('Hello world!')
  file.close()
def read_file():
  if path.isfile('./08-errors-files/files/text.txt'):
    file = open('./08-errors-files/files/text.txt', 'r')
    # texts = file.read()
    texts = file.readlines()
    file.close()
    print(texts)
  else:
    print('File doesn\t exist')
# write_file()
read_file()