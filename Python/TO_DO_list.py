print("1.ADD 2.VIEW 3.DELET(1/2/3)")
menu = input(">").lower()

def add():
    print("ADD new task")
    add_task = input("Enter your task")
    with open ('tile.txt','a') as f:
        f.write(add_task + "\n")

def view():
    print("Tasks")
    with open('tile.txt',"r") as f:
        print(f.read())

def delete():
    del_task = input("Enter the task to delete: ")

    # Read all lines
    with open("file.txt", "r") as f:
        lines = f.readlines()

    # Rewrite file without the deleted task
    with open("file.txt", "w") as f:
        found = False
        for line in lines:
            if line.strip() != del_task:
                f.write(line)
            else:
                found = True

    if found:
        print("Task deleted successfully")
    else:
        print("Task not found")

if menu == 'add' or menu == '1':
    add()
elif menu == 'view'or menu == '2':
    view()
elif menu == 'delet'or menu == '3':
    delete()
else:
    print('Invilad choice')
