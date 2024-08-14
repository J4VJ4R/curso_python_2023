import tkinter as tk
from tkinter import ttk
from model.model_movies import create_table, delete_table
from model.model_movies import Movie, save_movie, list_movies, edit_movie, delete_movie
from tkinter import messagebox

def menu_bar(root):
  menu_bar = tk.Menu(root)
  root.config(menu=menu_bar, width=300, height=300)
  menu_home = tk.Menu(menu_bar, tearoff=0)
  menu_bar.add_cascade(label='Home', menu = menu_home)

  menu_home.add_command(label='Create register on DB', command=create_table)
  menu_home.add_command(label='Delete register on DB', command=delete_table)
  menu_home.add_command(label='Exit', command = root.destroy)

  menu_bar.add_cascade(label='Queries', menu = menu_home)
  menu_bar.add_cascade(label='Configuration', menu = menu_home)
  menu_bar.add_cascade(label='Help', menu = menu_home)


class Frame(tk.Frame):
  #Construct
  def __init__(self, root = None):
    super().__init__(root, width=480, height=320)
    self.root = root
    self.pack()
    self.movie_id = None
    self.movie_fields()
    self.deactivate_fields()
    self.data_table()
  def movie_fields(self):
    #Labels of fields
    self.label_name = tk.Label(self, text = 'Name: ')
    self.label_name.config(font = ('Arial', 12, 'bold'))
    self.label_name.grid(row = 0, column = 0, padx=10, pady=10)

    self.label_duration = tk.Label(self, text = 'Duration: ')
    self.label_duration.config(font = ('Arial', 12, 'bold'))
    self.label_duration.grid(row = 1, column = 0, padx=10, pady=10)

    self.label_genre = tk.Label(self, text = 'Genre: ')
    self.label_genre.config(font = ('Arial', 12, 'bold'))
    self.label_genre.grid(row = 2, column = 0, padx=10, pady=10)

    #Entries for fields
    self.my_name = tk.StringVar()
    self.entry_name = tk.Entry(self, textvariable=self.my_name)
    self.entry_name.config(width=50, font=('Arial', 12))
    self.entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    self.my_duration = tk.StringVar()
    self.entry_duration = tk.Entry(self, textvariable=self.my_duration)
    self.entry_duration.config(width=50, font=('Arial', 12))
    self.entry_duration.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    self.my_genre = tk.StringVar()
    self.entry_genre = tk.Entry(self, textvariable=self.my_genre)
    self.entry_genre.config(width=50, font=('Arial', 12))
    self.entry_genre.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    #Buttons
    self.new_button = tk.Button(self, text='New', command=self.activate_fields)
    self.new_button.config(width=20, font=('Arial', 12, 'bold'),
                           fg='#DAD5D6', bg='#158645',
                           cursor='hand2', activebackground='#36bd6f')
    self.new_button.grid(row=3, column=0, padx=10, pady=10)

    self.save_button = tk.Button(self, text='Save', command=self.save_data)
    self.save_button.config(width=20, font=('Arial', 12, 'bold'),
                           fg='#DAD5D6', bg='#1658a2',
                           cursor='hand2', activebackground='#3586df')
    self.save_button.grid(row=3, column=1, padx=10, pady=10)

    self.cancel_button = tk.Button(self, text='Cancel', command=self.deactivate_fields)
    self.cancel_button.config(width=20, font=('Arial', 12, 'bold'),
                           fg='#DAD5D6', bg='#bd152e',
                           cursor='hand2', activebackground='#e15370')
    self.cancel_button.grid(row=3, column=2, padx=10, pady=10)

  def activate_fields(self):
    self.my_name.set('')
    self.my_duration.set('')
    self.my_genre.set('')

    self.entry_name.config(state='normal')
    self.entry_duration.config(state='normal')
    self.entry_genre.config(state='normal')

    self.save_button.config(state='normal')
    self.cancel_button.config(state='normal')

  def deactivate_fields(self):
    self.movie_id = None
    self.my_name.set('')
    self.my_duration.set('')
    self.my_genre.set('')

    self.entry_name.config(state='disabled')
    self.entry_duration.config(state='disabled')
    self.entry_genre.config(state='disabled')

    self.save_button.config(state='disabled')
    self.cancel_button.config(state='disabled')
  def save_data(self):
    movie = Movie(
      self.my_name.get(),
      self.my_duration.get(),
      self.my_genre.get(),
    )
    if self.movie_id == None:
      #Inserting movie
      save_movie(movie)
    else:
      edit_movie(movie, self.movie_id)      
    #Refresh list movies
    self.data_table()
    #Deactivate fields
    self.deactivate_fields()

  def data_table(self):
    #Get all data table
    self.list_movies = list_movies()
    self.list_movies.reverse()
    self.table = ttk.Treeview(self,
                              columns=('Name', 'Duration', 'Genre'))
    self.table.grid(row=4, column=0, columnspan=4, sticky='nse')

    #Scrollbar for table
    self.scroll = ttk.Scrollbar(self,
                                orient='vertical', command=self.table.yview)
    self.scroll.grid(row=4, column=4, sticky='nse')
    self.table.configure(yscrollcommand=self.scroll.set)

    self.table.heading('#0', text='ID')
    self.table.heading('#1', text='NAME')
    self.table.heading('#2', text='DURATION')
    self.table.heading('#3', text='genre')

    #Iteration on data table
    for movie in self.list_movies:
      #Insert data
      self.table.insert('', 0, text=movie[0],
                        values=(movie[1], movie[2], movie[3]))
    
    #Buttons

    #Edit
    self.edit_button = tk.Button(self, text='Edit', command=self.edit_data)
    self.edit_button.config(width=20, font=('Arial', 12, 'bold'),
                           fg='#DAD5D6', bg='#158645',
                           cursor='hand2', activebackground='#36bd6f')
    self.edit_button.grid(row=5, column=0, padx=10, pady=10)

    #Delete
    self.delete_button = tk.Button(self, text='Delete', command=self.delete_data)
    self.delete_button.config(width=20, font=('Arial', 12, 'bold'),
                           fg='#DAD5D6', bg='#bd152e',
                           cursor='hand2', activebackground='#e15370')
    self.delete_button.grid(row=5, column=1, padx=10, pady=10)

  def edit_data(self):
    try:
      self.movie_id = self.table.item(self.table.selection())['text']
      self.movie_name = self.table.item(self.table.selection())['values'][0]
      self.movie_duration = self.table.item(self.table.selection())['values'][1]
      self.movie_genre = self.table.item(self.table.selection())['values'][2]

      self.activate_fields()

      self.entry_name.insert(0, self.movie_name)
      self.entry_duration.insert(0, self.movie_duration)
      self.entry_genre.insert(0, self.movie_genre)
    except:
      title = 'Edit data'
      message = 'It wasn\'t selected any data'
      messagebox.showerror(title, message)

  def delete_data(self):
    try:
      self.movie_id = self.table.item(self.table.selection())['text']
      delete_movie(self.movie_id)
      title = 'Delete data'
      message = 'Data was deleted'
      messagebox.showinfo(title, message)
      self.data_table()
      self.movie_id = None
    except:
      title = 'Delete data'
      message = 'Data wasn\'t deleted'
      messagebox.showerror(title, message)
      


