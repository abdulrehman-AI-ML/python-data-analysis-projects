#Date = jan 20 ,2025

import random
count = 0
#loop
while True:
    print('Roll the Dice (y/n)')
    user =  input(">").lower()

    if user not in ['y','n']:
        print('Invilad choice')
    elif user == 'n':
        print(f'You roll the dies {count} times.')
        print('Thanks for playing! ')
        break
    else:
        count +=1
        die1 = random.randint(1,6)
        die2 =random.randint(1,6)
        print(f'({die1},{die2})')