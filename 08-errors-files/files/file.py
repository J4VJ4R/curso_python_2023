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
def add_data():
  if path.isfile('./08-errors-files/files/text.txt'):
    file = open('./08-errors-files/files/text.txt', 'a')
    file.write('\nHello Juan')
    file.close()
  else:
    print('File doesn\'t exist')
def update_data():
  if path.isfile('./08-errors-files/files/text.txt'):
    file = open('./08-errors-files/files/text.txt', 'r+')
    texts = file.readlines()
    texts[1] = 'Hello Pedro\n'
    # file.write('\nHello Javi')
    print(texts)
    file.seek(0)
    file.writelines(texts)
    file.close()
    print(texts)
def delete_data():
  file = open('./08-errors-files/files/text.txt', 'w')
  file.close()
# write_file()
# read_file()
# add_data()
# update_data()
delete_data()