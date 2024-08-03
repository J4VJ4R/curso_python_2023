from pets import Pet, RegisterPets

registration = RegisterPets()

while True:
  menu = """
  --- MENU ---
  1 - Add pet
  2 - List pets
  3 - Edit pet
  4 - Delete pet
  5 - Exit
  Type an option: 
"""

  option = input(menu)
  if option == "1":
    type_animal = input("Type the pet's type: ")
    age = input("Type the pet's age: ")
    name = input("Type the pet's name: ")

    pet = Pet(type_animal, age, name)
    registration.addPet(pet)
  elif option == "2":
    registration.listPets()
  elif option == "3":
    index = int(input("Type index: "))
    type_animal = input("Type the pet's type: ")
    age = input("Type the pet's age: ")
    name = input("Type the pet's name: ")

    newpet = Pet(type_animal, age, name)
    registration.editPet(index - 1 , newpet)
  elif option == "4":
    index = int(input("Type index to delete: "))
    registration.deletePet(index - 1)
  elif option == "5":
    print("Bye...")
    break
  else:
    print("Invalid option, type your option again.")