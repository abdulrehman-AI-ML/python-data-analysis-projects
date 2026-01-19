#inputs
import random

computer = random.choice(["Rook","Paper","Scissors"])
print(computer)

while True:
    menu = input("Start Or End (s/e): ").lower()
    if menu not in ['s','Start','start']:
        print('Have a Good day!')
        break
    else:
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