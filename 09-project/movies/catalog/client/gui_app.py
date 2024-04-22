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
    self.config(bg='green')