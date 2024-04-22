import tkinter as tk

def menu_bar(root):
  bar_menu = tk.Menu(root)
  root.config(menu = bar_menu, width=300, height = 300)

  main_menu = tk.Menu(bar_menu, tearoff=0)
  bar_menu.add_cascade(label='Home', menu = main_menu)
  main_menu.add_command(label='Create register on DB')
  main_menu.add_command(label='Delete register on DB')
  main_menu.add_command(label='Exit', command=root.destroy)

  query_data = tk.Menu(bar_menu, tearoff=0)
  bar_menu.add_cascade(label='Query Data', menu=query_data)
  query_data.add_command(label='Test1')

  bar_menu.add_cascade(label='Config')
  bar_menu.add_cascade(label='Help')

class Frame(tk.Frame):
  def __init__(self, root = None):
    super().__init__(root, width=480, height=320 )
    self.root = root
    self.pack()
    # self.config(bg='green')

    self.movies_fields()
  def movies_fields(self):
    #Labels for fields
    #Row for name
    self.name_label = tk.Label(self, text = 'Name: ')
    self.name_label.config(font = ('Arial', 12, 'bold'))
    self.name_label.grid(row = 0, column = 0, padx=10, pady=10)
    #Row for Duration
    self.name_label = tk.Label(self, text = 'Duration: ')
    self.name_label.config(font = ('Arial', 12, 'bold'))
    self.name_label.grid(row = 1, column = 0, padx=10, pady=10)
    #Row for Genre
    self.name_label = tk.Label(self, text = 'Genre: ')
    self.name_label.config(font = ('Arial', 12, 'bold'))
    self.name_label.grid(row = 2, column = 0, padx=10, pady=10)
    #Entries for fields
    self.entry_name = tk.Entry(self)
    self.entry_name.config(width=50, state='disabled', font=('Arial', 12))
    self.entry_name.grid(row=0, column=1, padx=10, pady=10)
    self.entry_duration = tk.Entry(self)
    self.entry_duration.config(width=50, state='disabled', font=('Arial', 12))
    self.entry_duration.grid(row=1, column=1, padx=10, pady=10)
    self.entry_genre = tk.Entry(self)
    self.entry_genre.config(width=50, state='disabled', font=('Arial', 12))
    self.entry_genre.grid(row=2, column=1, padx=10, pady=10)