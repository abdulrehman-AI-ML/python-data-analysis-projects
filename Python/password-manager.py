master_pass = input("Enter the master password: ")

def view():
    try:
        with open("password.txt", "r") as f:
            for line in f.readlines():
                data = line.rstrip()
                name, password = data.split("/")
                print(f"Name: {name} | Password: {password}")
    except FileNotFoundError:
        print("No passwords stored yet.")

def add():
    name = input("Enter the name: ")
    password = input("Enter the password: ")

    with open("password.txt", "a") as f:
        f.write(name + "/" + password + "\n")

while True:
    mode = input(
        "Would you like to add a password or view existing ones? (add/view, q to quit): "
    ).lower()

    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid choice")
