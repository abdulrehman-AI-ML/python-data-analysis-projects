import random 
import string

password = {}

try:
    with open('file.txt','r') as f:
        for line in f:
            website,pwd = line.strip().spilt(":")
            password[website] = pwd 
except:
    pass

def genrate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("------ Password Manegar App ---------")

    print("1- Add Password")
    print("2- view password")
    print("3- Genrate password")
    print("4- Exit")

    user  = input("Enter the your option: ").lower()

    if user in ("1","add password"):
        site = input("Enter website: ")
        pwd = input("Enter Password: ")
        password[site] = pwd
        with open("file.txt","a") as f:
            f.write(site+":"+pwd+"\n")
        print("Password saved successfuly stored")


    elif user in ("2","view password","view passwords"):
        if not password:
            print("no data found")
        else:
            view = input("Enter the site: ")
            with open ("file.txt","r") as f:
                for line in f:
                    if view in line :
                        print (f"{view.item()}")

    elif user in ("4","exit",'stop'):
        print("program ended")