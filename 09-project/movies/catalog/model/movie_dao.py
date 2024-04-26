from .conection_db import ConectionDB

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

  conection1.cursor.execute(sql)
  conection1.close()

def delete_table():
  conection2 = ConectionDB()

  sql = 'DROP TABLE movies'

  conection2.cursor.execute(sql)
  conection2.close()