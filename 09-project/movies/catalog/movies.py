import tkinter as tk
from client.gui_app import Frame
def main():
  root = tk.Tk()
  root.title('Movies Catalog')
  # root.iconbitmap('09-project/movies/catalog/img/mov2.png')
  root.resizable(0,0)

  app = Frame(root = root)
  app.mainloop()

if __name__ == '__main__':
  main()