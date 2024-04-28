import tkinter as tk
from tkinter import ttk
from model.movie_dao import create_table, delete_table
from model.movie_dao import Movie, save, showdata
def menu_bar(root):
  bar_menu = tk.Menu(root)
  root.config(menu = bar_menu, width=300, height = 300)

  main_menu = tk.Menu(bar_menu, tearoff=0)
  bar_menu.add_cascade(label='Home', menu = main_menu)
  main_menu.add_command(label='Create register on DB', command=create_table)
  main_menu.add_command(label='Delete register on DB', command=delete_table)
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
    self.fields_disabled()
    self.movies_table()
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
    self.my_name = tk.StringVar()
    self.entry_name = tk.Entry(self, textvariable=self.my_name)
    self.entry_name.config(width=50, font=('Arial', 12))
    self.entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2)
    self.my_duration = tk.StringVar()
    self.entry_duration = tk.Entry(self, textvariable=self.my_duration)
    self.entry_duration.config(width=50,  font=('Arial', 12))
    self.entry_duration.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
    self.my_genre = tk.StringVar()
    self.entry_genre = tk.Entry(self, textvariable=self.my_genre)
    self.entry_genre.config(width=50, font=('Arial', 12))
    self.entry_genre.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
    #Button new
    self.new_button = tk.Button(self, text="New", command=self.fields_available)
    self.new_button.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', 
                          bg='#158645', cursor='hand2', activebackground='#35BD6F')
    self.new_button.grid(row=3, column=0, padx=10, pady=10)
    #Button save
    self.save_button = tk.Button(self, text="Save", command=self.save_data)
    self.save_button.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', 
                          bg='#1658A2', cursor='hand2', activebackground='#3586DF')
    self.save_button.grid(row=3, column=1, padx=10, pady=10)
    #Button cancel
    self.cancel_button = tk.Button(self, text="Cancel", command=self.fields_disabled)
    self.cancel_button.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', 
                          bg='#BD152E', cursor='hand2', activebackground='#E15370')
    self.cancel_button.grid(row=3, column=2, padx=10, pady=10)

  def fields_available(self):
    #Entry configuration
    #Clean fields
    self.my_name.set('')
    self.my_duration.set('')
    self.my_genre.set('')
    #Change state fields
    self.entry_name.config(state='normal')
    self.entry_duration.config(state='normal')
    self.entry_genre.config(state='normal')
    #Buttons configuration
    self.save_button.config(state='normal')
    self.cancel_button.config(state='normal')
  def fields_disabled(self):
    #Entry configuration
    #Clean fields
    self.my_name.set('')
    self.my_duration.set('')
    self.my_genre.set('')
    #Change state fields
    self.entry_name.config(state='disabled')
    self.entry_duration.config(state='disabled')
    self.entry_genre.config(state='disable')
    #Buttons configuration
    self.save_button.config(state='disable')
    self.cancel_button.config(state='disable')
  def save_data(self):
    movie = Movie(
      self.my_name.get(),
      self.my_duration.get(),
      self.my_genre.get(),
    )
    #Movie objetc was create
    #Save data
    save(movie)
    #Update table
    self.movies_table()
    self.fields_disabled()
  def movies_table(self):
    #Recover movies
    self.list_movies = showdata()
    self.list_movies.reverse()
    #Create table
    self.table = ttk.Treeview(self, columns=('Name', 'Duration', 'Genre'))
    self.table.grid(row=4, column=0, columnspan=4)
    #Headers names
    self.table.heading('#0', text='ID')
    self.table.heading('#1', text='NAME')
    self.table.heading('#2', text='DURATION')
    self.table.heading('#3', text='GENRE')
    #Fill some data
    #Iteration of movies
    for movie in self.list_movies:
      self.table.insert('', 0, text=movie[0], values=(movie[1], movie[2], movie[3]))
    #Button editar
    self.edit_button = tk.Button(self, text="Edit")
    self.edit_button.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', 
                          bg='#158645', cursor='hand2', activebackground='#35BD6F')
    self.edit_button.grid(row=5, column=0, padx=10, pady=10)
    #Button eliminar
    self.cancel_button = tk.Button(self, text="Delete")
    self.cancel_button.config(width=20, font=('Arial', 12, 'bold'), fg='#DAD5D6', 
                          bg='#BD152E', cursor='hand2', activebackground='#E15370')
    self.cancel_button.grid(row=5, column=1, padx=10, pady=10)