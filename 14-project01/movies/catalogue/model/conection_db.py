import sqlite3

class ConectionDB:
  def __init__(self):
    self.database = 'database/movies.db'
    self.conection = sqlite3.connect(self.database)
    self.cursor = self.conection.cursor()

  #Close database
  def close_database(self):
    self.conection.commit()
    self.conection.close()