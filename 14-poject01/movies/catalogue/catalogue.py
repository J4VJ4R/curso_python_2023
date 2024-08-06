import tkinter as tk
from client.gui_app import Frame, menu_bar

def main():
  root = tk.Tk()
  root.title("Catalogue")
  root.iconbitmap('../img/movie.ico')
  root.resizable(0,0)

  app = Frame(root = root)
  menu_bar(root)
  app.mainloop()

if __name__ == "__main__":
  main()