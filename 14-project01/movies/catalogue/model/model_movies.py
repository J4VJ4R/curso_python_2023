from .conection_db import ConectionDB
from tkinter import messagebox

def create_table():
  conection = ConectionDB()

  #Creating table
  sql = '''
  CREATE TABLE movies(
    id_movie INTEGER,
    name VARCHAR(100),
    duration VARCHAR(10),
    genre VARCHAR(100),
    PRIMARY KEY(id_movie AUTOINCREMENT)
  )
  '''
  try:
    conection.cursor.execute(sql)
    conection.close_database()
    title = 'Create Registers'
    message = 'It was create a table on database'
    messagebox.showinfo(title, message)
  except:
    title = 'Create Registers'
    message = 'It was not create the table on database'
    messagebox.showwarning(title, message)

def delete_table():
  conection = ConectionDB()

  sql = 'DROP TABLE movies'
  try:
    conection.cursor.execute(sql)
    conection.close_database()
    title = 'Delete register'
    message = 'It was deleted database'
    messagebox.showinfo(title, message)
  except:
    title = 'Delete register'
    message = 'There isn\'t any database to delete'
    messagebox.showerror(title, message)

class Movie:
  def __init__ (self, name, duration, genre):
    self.id_movie = None
    self.name = name
    self.duration = duration
    self.genre = genre

  def __str__(self):
    return f'Movies[{self.name}, {self.duration}, {self.genre}]'
  
def save_movie(movie):
  conection = ConectionDB()

  sql = f"""INSERT INTO movies (name, duration, genre)
  VALUES('{movie.name}', '{movie.duration}', '{movie.genre}')"""

  try:
    conection.cursor.execute(sql)
    conection.close_database()
  except:
    title = 'Conection Register'
    message = 'Table Movie doesn\'t exist'
    messagebox.showerror(title, message)

def list_movies():
  conection = ConectionDB()
  list_movies = []
  
  sql = 'SELECT * FROM movies'

  try:
    conection.cursor.execute(sql)
    list_movies = conection.cursor.fetchall()
    conection.close_database()
  except:
    title = 'Register conection'
    message = 'It doesn\t any data'
    messagebox.showerror(title, message)
  return list_movies

def edit_movie(movie, movie_id):
  conection = ConectionDB()
  sql = f"""UPDATE movies
  SET name = '{movie.name}', duration = '{movie.duration}', genre = '{movie.genre}'
  WHERE id_movie = {movie_id}"""

  try:
    conection.cursor.execute(sql)
    conection.close_database()
  except:
    title = 'Data edit'
    message = 'An error has ocurred here'
    messagebox.showerror(title, message)

def delete_movie(movie_id):
  conection = ConectionDB()
  sql = f"DELETE FROM movies WHERE id_movie = {movie_id}"

  try:
    conection.cursor.execute(sql)
    conection.close_database()
  except:
    title = 'Delete data'
    message = "Data wasn't deleted"
    messagebox.showinfo(title, message)