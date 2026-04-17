""" 
Teacher:
1- add student
2- view all student
3- check result
4- exit

"""
student_name = {}

print("------Student Manegar App---------")

print("1- Add student")
print("2- view students")
print("3- check result")
print("4- Exit")

menu = input('>Chose your option: ').lower()

if menu in ("1" ,"add student"):
    name = input("Enter the student name:")
    marks = int(input("Enter the student marks"))
    student_name[name] = marks
elif menu in ("2" ,"view student"):
    
else:
    print('wronge')