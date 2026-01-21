# asking user for master password
master_pass = input("Enter the master password: ")

# function to view saved passwords
def view():
    try:
        # opening file in read mode
        with open("password.txt", "r") as f:
            for line in f.readlines():
                # removing extra spaces and new line
                data = line.rstrip()
                # splitting name and password
                name, password = data.split("/")
                print("Name:", name, "| Password:", password)
    except FileNotFoundError:
        # if file does not exist
        print("No passwords stored yet.")

# function to add new password
def add():
    # taking name and password from user
    name = input("Enter the name: ")
    password = input("Enter the password: ")

    # opening file in append mode to save data
    with open("password.txt", "a") as f:
        f.write(name + "/" + password + "\n")

# running program in loop
while True:
    # asking user what they want to do
    mode = input(
        "Would you like to add a password or view existing ones? (add/view, q to quit): "
    ).lower()

    # if user wants to quit
    if mode == "q":
        break

    # if user wants to view passwords
    elif mode == "view":
        view()

    # if user wants to add password
    elif mode == "add":
        add()

    # if user enters wrong option
    else:
        print("Invalid choice")
