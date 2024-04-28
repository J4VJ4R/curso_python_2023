from .conection_db import ConectionDB
from tkinter import messagebox

def create_table():
  conection1 = ConectionDB()

  sql = '''
  CREATE TABLE movies(
    id_movie INTEGER, 
    name VARCHAR(100),
    duration VARCHAR(10),
    genre  VARCHAR(100),
    PRIMARY KEY(id_movie AUTOINCREMENT)
  )'''
  try:
    conection1.cursor.execute(sql)
    conection1.close()
    title = 'Create Register'
    message = 'It\'s created table on database'
    messagebox.showinfo(title, message)
  except:
    title = 'Create Register'
    message = 'The table was already created'
    messagebox.showwarning(title, message)
#Function to delete table
def delete_table():
  conection2 = ConectionDB()

  sql = 'DROP TABLE movies'
  try:
    conection2.cursor.execute(sql)
    conection2.close()
    title = 'Delete Register'
    message = 'The table was deleted sucessfully'
    messagebox.showinfo(title, message)
  except:
    title = 'Delete Register'
    message = 'There isn\'t table to delete'
    messagebox.showerror(title, message)
class Movie:
  def __init__(self, name, duration, genre):
    self.id_movie = None
    self.name = name
    self.duration = duration
    self.genre = genre

  def __str__(self):
    return f'Movie[{self.name}, {self.duration}, {self.genre}]'

def save(movie):
  conection = ConectionDB()

  sql = f"""
    INSERT INTO movies (name, duration, genre)
    VALUES('{movie.name}', '{movie.duration}', '{movie.genre}')
  """
  try:
    conection.cursor.execute(sql)
    conection.close()
  except:
    title = 'Conection register'
    message = 'The table movie doesn\'t is created'
    messagebox.showerror(title, message)

def showdata():
  conection = ConectionDB()

  list_movies = []
  sql = """SELECT * FROM movies"""

  try:
    conection.cursor.execute(sql)
    list_movies = conection.cursor.fetchall()
    conection.close()
  except:
    title = 'Conection to register'
    message = 'Create table on databases'
    messagebox.showwarning(title, message)
  
  return list_movies
