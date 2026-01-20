
#Date = 20 jan ,2025

import random
#computer choice a random move 
computer = random.choice(["Rook","Paper","Scissors"])
print(computer)

#useing loops to run it again and again until user stop it 
while True:
    #input to start or end the game
    menu = input("Start Or End (s/e): ").lower()
    #end 
    if menu not in ['s','Start','start']:
        print('Have a Good day!')
        break
    #start
    else:
        #simple moves with some conditions 
        print("Choose your move Rook ,Paper ,Scissor")
        person = input("> ").lower()
        if computer  == person:
            print('its a tie')
        elif person == 'rock' and computer == 'scissor':
            print(f"Computer choice {computer} and you choice {person}")
            print("You won!")
        elif person == 'scissor' and computer == 'paper':
            print(f"Computer choice {computer} and you choice {person}")
            print("You won!")
        elif person == 'paper' and computer == 'rock':
            print(f"Computer choice {computer} and you choice {person}")
            print("You won!")
        else:
            print(f"Computer choice {computer} and you choice {person}")
            print("Computer win!")