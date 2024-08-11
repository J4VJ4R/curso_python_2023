import tkinter as tk
from tkinter import ttk
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
  #Construct
  def __init__(self, root = None):
    super().__init__(root, width=480, height=320)
    self.root = root
    self.pack()
    # self.config(bg='green')
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

    self.label_gender = tk.Label(self, text = 'gender: ')
    self.label_gender.config(font = ('Arial', 12, 'bold'))
    self.label_gender.grid(row = 2, column = 0, padx=10, pady=10)

    #Entries for fields
    self.my_name = tk.StringVar()
    self.entry_name = tk.Entry(self, textvariable=self.my_name)
    self.entry_name.config(width=50, font=('Arial', 12))
    self.entry_name.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

    self.my_duration = tk.StringVar()
    self.entry_duration = tk.Entry(self, textvariable=self.my_duration)
    self.entry_duration.config(width=50, font=('Arial', 12))
    self.entry_duration.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    self.my_gender = tk.StringVar()
    self.entry_gender = tk.Entry(self, textvariable=self.my_gender)
    self.entry_gender.config(width=50, font=('Arial', 12))
    self.entry_gender.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

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
    self.my_gender.set('')

    self.entry_name.config(state='normal')
    self.entry_duration.config(state='normal')
    self.entry_gender.config(state='normal')

    self.save_button.config(state='normal')
    self.cancel_button.config(state='normal')

  def deactivate_fields(self):
    self.my_name.set('')
    self.my_duration.set('')
    self.my_gender.set('')

    self.entry_name.config(state='disabled')
    self.entry_duration.config(state='disabled')
    self.entry_gender.config(state='disabled')

    self.save_button.config(state='disabled')
    self.cancel_button.config(state='disabled')
  def save_data(self):
    self.deactivate_fields()

  def data_table(self):
    self.table = ttk.Treeview(self,
                              columns=('Name', 'Duration', 'Gender'))
    self.table.grid(row=4, column=0, columnspan=4)

    self.table.heading('#0', text='ID')
    self.table.heading('#1', text='NAME')
    self.table.heading('#2', text='DURATION')
    self.table.heading('#3', text='GENDER')

    #Insert data
    self.table.insert('', 0, text='1',
                      values=('Avengers', '2.35', 'Action'))
    
    #Buttons

    #Edit
    self.edit_button = tk.Button(self, text='Edit')
    self.edit_button.config(width=20, font=('Arial', 12, 'bold'),
                           fg='#DAD5D6', bg='#158645',
                           cursor='hand2', activebackground='#36bd6f')
    self.edit_button.grid(row=5, column=0, padx=10, pady=10)

    #Cancel
    self.delete_button = tk.Button(self, text='Delete')
    self.delete_button.config(width=20, font=('Arial', 12, 'bold'),
                           fg='#DAD5D6', bg='#bd152e',
                           cursor='hand2', activebackground='#e15370')
    self.delete_button.grid(row=5, column=1, padx=10, pady=10)


