""" 
Teacher:
1- add student
2- view all student
3- check result
4- update marks
5- delete student
6- exit

"""
students = {}
while True:
    print("------Student Manegar App---------")

    print("1- Add student")
    print("2- view students")
    print("3- check result")
    print("4- update marks")
    print("5- delete student")
    print("6- Exit")

    menu = input('>Chose your option: ').lower()
#========== add student =========#
    if menu in ("1" ,"add student"):
        name = input("Enter the student name:")
        marks = int(input("Enter the student marks:"))
        students[name] = marks
        print(f'{name} is successfuly added')
#========== view student=========#
    elif menu in ("2" ,"view student"):
        if not students:
            print("No student found!")
        else:
            for name,marks in students.items():
                print(f"Name   Marks\n {name} : {marks}")
#========== Check result =========#
    elif menu in ("3","check result"):
        student_name = input("Enter the student name: ")
        if student_name in students:
           marks = students[name]
           if marks >=40:
               print('Pass')
           else:
               print("Fail")
        else:
            print("Student not found")
#============= update marks =========#
    elif menu in ("4",'update marks'):
        student_name = input("Enter the student name: ")
        if student_name in students:
            students[student_name] = int(input('Enter new marks: '))
            print(f"{student_name}'s marks updated to {students[student_name]}")
        else:
            print("Student not found")

#============= delete student =========#
    elif menu in ("5",'delete student'):
        student_name = input("Enter the student name: ")
        if student_name in students:
            del students[student_name]
            print(f"{student_name} has been deleted.")
        else:
            print("Student not found")

        
#========== Exit =========#
    elif menu in ('6','exit'):
        print("GOOD BYE")
        break
    else:
        print('Enter the correct option')
    