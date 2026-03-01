import os
import time
main = input("1.New account 2.Existed account(1,2):\n>").lower()


def new():
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
    




if main == '1' or main == "new account":
    pin = input("set you pin:")
    #addasdadsad