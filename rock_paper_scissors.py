import random
def RPS():
    # We are going to start by giving the computer a list with the options of rock paper scissors
    def computerplayer():
    ComChoices = ['Rock', 'Paper', 'Scissors']

    # I'm going to try to use randomchoice to get a random string from the computers option
    Computer = random.choice(ComChoices)

    # Now I need to identify the user and give him/her an input

    Player = input('Rock, Paper, Scissors, or quit?')

    # I need to make a while loop to allow there to be multiple games played
    # Or i could leave it without and only have one
    #but i think it'll be better with a while loop

    playing = True 
    #need if statments to def what wins and what loses in the game
    while playing:
    

    # THIS WAS GOING TO BE MY ATTEMPT BUT WITHOUT A FUNCTION AND I REMEBERED THAT IS A NO GO
