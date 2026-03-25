import os
import time
main = input("1.New account 2.Existed account(1,2):\n>").lower()


if main == "1" or main == 'new account':
    new()
elif main == '2' or main == 'existed account':
    existed()



def existed():
    setpin = input("Enter your pin: ")
    file_path=  fr"M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{setpin}.txt"
    with open (file_path,"r") as f:
        f.read()    
    print('Your account is opend')
    edit_acc = int(input('View or add money (1,2):'))
    if edit_acc == 1:
        with open (file_path,'r') as f:
            print(f.read())
    elif edit_acc == 2:
        n_add_balance = int(input("Enter you balance:"))
        with open (file_path,'a') as f:
            print(f.write(n_add_balance))
    else :
        print("Something is wrong!")
    


def new():
    pin = input("set you pin:")
    with open(f'M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{pin}','r') as f:
        f.read()
    print("Your account is opend")
    edit_acc = int(input('View or add money (1,2):'))
    if edit_acc == 1:
        with open(f'M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{pin}','r') as f:
            f.read()
    elif edit_acc == 2 :
        with open (f'M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{pin}','a') as f:
            n_add_balance = int(input("Enter you balance:"))
            f.write(n_add_balance)
            print(f"{n_add_balance} has been added to your account")
    else:
        print('something wronge!!')