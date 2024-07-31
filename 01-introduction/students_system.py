students_list = []
print("-"*30)
print("------     WELCOME    ------")
print("------ STUDENTS SYSTEM ------")
print("-"*30)

while True:
  option = input("""
    CHOSE ONE OPTION
                              
    1 - Register Students
    2 - View Students
    3 - Close System 
    
    --> 
  """)
  if option == "1":
    #Variables
    name = input("Type name: ")
    age = int(input("Type age: "))
    course = input("Type course: ")
    #Dictionaries of student
    student = {"name":name, "age":age, "course": course}
    #List of students
    students_list.append(student)
    print("Register succesfulled!!\n")
  elif option == "2":
    if students_list:
      print("Students Register")
      for student in students_list:
        print(f"Name: {student["name"]}, Age: {student["age"]}, Course: {student["course"]}")
    else:
      print("The register is empty, register one student before..")  
  elif option == "3":
    print("Closing program...")  
    break
  else:
    print("Invalide option, try egain.\n")
