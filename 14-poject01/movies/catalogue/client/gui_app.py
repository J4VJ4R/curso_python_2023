import tkinter as tk

def menu_bar(root):
  menu_bar = tk.Menu(root)
  root.config(menu=menu_bar, width=300, height=300)
  menu_home = tk.Menu(menu_bar, tearoff=0)
  menu_bar.add_cascade(label='Home', menu = menu_home)

  menu_home.add_command(label='Create register on DB')
  menu_home.add_command(label='Delete register on DB')
  menu_home.add_command(label='Exit', command = root.destroy)

  menu_bar.add_cascade(label='Queries', menu = menu_home)
  menu_bar.add_cascade(label='Configuration', menu = menu_home)
  menu_bar.add_cascade(label='Help', menu = menu_home)


class Frame(tk.Frame):
  def __init__(self, root = None):
    super().__init__(root, width=480, height=320)
    self.root = root
    self.pack()
    # self.config(bg='green')
    self.movie_fields()

  def movie_fields(self):
    #Labels of fields
    self.label_name = tk.Label(self, text = 'Name: ')
    self.label_name.config(font = ('Arial', 12, 'bold'))
    self.label_name.grid(row = 0, column = 0, padx=10, pady=10)

    self.label_duration = tk.Label(self, text = 'Duration: ')
    self.label_duration.config(font = ('Arial', 12, 'bold'))
    self.label_duration.grid(row = 1, column = 0, padx=10, pady=10)

    self.label_genere = tk.Label(self, text = 'Genere: ')
    self.label_genere.config(font = ('Arial', 12, 'bold'))
    self.label_genere.grid(row = 2, column = 0, padx=10, pady=10)