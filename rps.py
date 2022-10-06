import random
import os
# since my input will only be rock paper scissors or quit
# I am making 4 different functions for each
#Need a couple of variables 
# Computer list with random generator
# player input

#after need to define what happens if user chooses rock paper or scissors and how the functions will work    
# ComChoices = ['Rock', 'Paper', 'Scissors']
# Computer = random.choice(ComChoices)
def rock(Player, Computer):
    os.system('cls')
    print(f'Rock, Paper, Scissors SHOOT!\n')
    print(f'p1 : {Player.title()} \ncpu : {Computer}')
    if Computer == 'Rock' and Player == 'Rock':
        print("\nLET'S PLAY AGAIN WE TIED")
    elif Computer == 'Paper' and Player == 'Rock':
        print("\nHaha I beat you human!")
    elif Computer == 'Scissors' and Player == 'Rock':
        print("\nError. I can't possibly lose again.")
    rps()

def paper(Player, Computer): 
    os.system('cls')
    print(f'Rock, Paper, Scissors SHOOT!\n')
    print(f'p1 : {Player.title()} \ncpu : {Computer}')
    if Computer == 'Rock' and Player == 'Paper':
        print("\nError. I can't possibly lose again.")
    elif Computer == 'Paper' and Player == 'Paper':
        print("\nLET'S PLAY AGAIN WE TIED")
    elif Computer == 'Scissors' and Player == 'Paper':
        print("\nHaha I beat you human!")
    rps()

def scissors(Player, Computer): 
    os.system('cls')
    print(f'Rock, Paper, Scissors SHOOT!\n')
    print(f'p1 : {Player.title()} \ncpu : {Computer}')
    if Computer == 'Rock' and Player == 'Scissors':
        print("\nHaha I beat you human!")
    elif Computer == 'Paper' and Player == 'Scissors':
        print("\nError. I can't possibly lose again.")
    elif Computer == 'Scissors' and Player == 'Scissors':
        print("\nLET'S PLAY AGAIN WE TIED")
    rps()

def quit():
     print(f'thanks for playing! the total for the wins and losses for todays game are ')

#-------Main Body-----





def rps():
    ComChoices = ['Rock', 'Paper', 'Scissors']
    Computer = random.choice(ComChoices)
    Player = input('Rock, Paper, Scissors, or quit?\n').title()
    #player varible will start the function

    if Player == 'Rock'.title():
        rock(Player, Computer)
    elif Player == 'Paper'.title():
        paper(Player, Computer)
    elif Player == 'Scissors'.title():
        scissors(Player, Computer)
    elif Player == 'quit'.title():
        quit()
rps()
        
        




    