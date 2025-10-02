# Student registrerings system
# Needs
# Data struktur för studenter
# Loop för menyn
# Menyn har 3 val: 1. Add student 2: List students 3: Quit
test_student = {"name": "Adam", "age": "21"}
student_list = [start_student] # Default student
max_num_students_to_print = 10
print ("Welcome to the student register!")
while True:
    print(" 1. Add student")
    print ("2. List student")
    print ("3. Quit")
    menu_choice = input (" Choose 1-3:")
    if menu_choice == "1":
        new_student_name = input("New student name ")
        new_student_age = input("New student age: ")
        new_student_dict = {"name": new_student_name, "age": new_student_age}
        print ("New student created" )
        print (f"Name:"{new_student_dict["name"]}, Age: {new_student_dict["age"]})
        student_list.append(new_student_dict)
        print (f"new_student_age")
    elif menu_choice == "2":
        for student in student_list:
            print(f"Name:"{student["Name"], "Age:" {student["age"]}}
    elif menu_choice =="3":
        print ("Student: ")
        print(student_list)
        quit()
    else:
        quit()



