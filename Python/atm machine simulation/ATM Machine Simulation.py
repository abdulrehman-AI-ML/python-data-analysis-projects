import os
import time


def existed():
    setpin = input("Enter your pin(Enter e to exist): ")
    print("checking...")
    time.sleep(2)
    while True:
        
        if os.path.exists(fr"M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{setpin}.txt") :
            print("account is found")
            with open(fr"M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{setpin}.txt",'r') as f:
                cur_bal =f.read()
            mainu = input('View, add, withdraw money (1,2,3):').lower()
            if mainu in ('view',"1"):
                with open(fr"M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{setpin}.txt",'r') as f:
                   cur_bal =float(f.read())
                   print(cur_bal)
            elif mainu in ('add','2'):
                with open(fr"M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{setpin}.txt",'r') as f:
                   cur_bal = float(f.read())
                with open(fr"M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{setpin}.txt",'w') as f:
                    add_balance = float(input('Enter the amount :'))
                    cur_bal = add_balance +cur_bal
                    cur_bal = str(cur_bal)
                    f.write(cur_bal)
                    print(cur_bal)
                    print('amount has been added to you account.')
            elif mainu in ('withdraw','3'):
                w_bal = float(input('enter the withdraw amount:'))
                if w_bal > cur_bal:
                    print("pls enter vail amount ")
                    print(f"you have {cur_bal}")
                else:
                    cur_bal= cur_bal - w_bal
                    with open(fr"M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{setpin}.txt",'w') as f:
                        f.write(cur_bal)
                    print(f"{w_bal} has be withdraw now you have {cur_bal}")
            
        else:
            print("account is not found")
            print('try again')
            continue
            
    
            
    
    


def new():
    pin = input("set you pin:")
    with open(fr'M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{pin}.txt','w') as f:
        f.write("0")
    print("Your account is opend")
    edit_acc = (input('View or add money (1,2):')).lower()
    if edit_acc  in ('view','1'):
        with open(fr'M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{pin}.txt','r') as f:
            f.read()
    elif edit_acc in ('add money','2') :
        with open (fr'M:\repos\python-data-analysis-projects\Python\atm machine simulation\accounts\{pin}.txt','w') as f:
            n_add_balance = float(input("Enter you balance:"))
            f.write(n_add_balance)
            print(f"{n_add_balance} has been added to your account")
    else:
        print('something wronge!!')

main = input("1.New account 2.Existed account(1,2):\n>").lower()

if main == "1" or main == 'new account':
    new()
elif main == '2' or main == 'existed account':
    existed()

