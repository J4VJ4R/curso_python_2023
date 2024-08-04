try:
  with open("13-errors/file.txt", "r") as file:
    content = file.read()

except FileNotFoundError:
  print("No any file was find")
  print("Creating the file")
  with open("13-errors/file.txt", "w") as file:
    file.write("Hello spacecode...")
else:
  print("Content of file")
  print(content)