import random 

computer = random.randint(1,5)
print('You have 5 try to guess the number from 1 to 100')
trys = 5

while True:
    try:
        user = int(input("Guess the number: "))
    except ValueError:
        print("Pls enter a valid number")
    if computer == user:
        print(f'You guess correct {computer} is right!')
        break
    elif trys == 1:
        print('You lose')
        break
    elif computer != user:
        print(f'{user} is not correct...')
        if computer > user:
            print('Enter greater number')
        elif computer < user:
            print('Enter shorter number')
        trys -=1
        print(f'you left {trys} guss')
        
    #comment

    