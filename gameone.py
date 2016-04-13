import random

def getuserinfo():
    print("Time to play")
    print("Whats your name?>")
    name=input("")
    print("1V1 or vs. Sheldon?",name,"?")
    decision=input("")
    decision.lower
    if decision=="1v1":
        playfriend()
    else:
        print("can you beat Sheldon",name,"?")
        playgame()

def playfriend():
    print("Rock, Paper, Scissors, Lizard, or Spock?")
    choice=input("")
    choice.lower
    Sheldon=input("")
    Sheldon.lower
    print("Player 1 chose", choice)
    print("Player 2 chose", Sheldon)
    if Sheldon==choice:
        print("its a tie")
    elif Sheldon=="rock":
        if choice==("lizard","scissors"):
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")
    elif Sheldon=="paper":
        if choice==("rock","spock"):
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")
    elif Sheldon=="scissors":
        if choice==("paper","lizard"):
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")
    elif Sheldon=="lizard":
        if choice==("spock","paper"):
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")
    elif Sheldon=="spock":
        if choice==("scissors","rock"):
            print("Player 2 Wins")
        else:
            print("Player 1 Wins")


def playgame():
    print("Rock, Paper, Scissors, Lizard, or Spock?")
    choice=input("")
    choice.lower
    Sheldon=random.random()
    if Sheldon <= .20:
        Sheldon="scissors"
    elif Sheldon <= .40:
        Sheldon="rock"
    elif Sheldon <= .60:
        Sheldon="paper"
    elif Sheldon <= .80:
        Sheldon="lizard"
    else:
        Sheldon="spock"
    print("Sheldon chose", Sheldon)

    if Sheldon==choice:
        print("its a tie")
    elif Sheldon=="rock":
        if choice==("lizard","scissors"):
            print("Sheldon Wins")
        else:
            print("YOU WIN!!")
    elif Sheldon=="paper":
        if choice==("rock","spock"):
            print("Sheldon Wins")
        else:
            print("YOU WIN!!")
    elif Sheldon=="scissors":
        if choice==("paper","lizard"):
            print("Sheldon Wins")
        else:
            print("YOU WIN!!")
    elif Sheldon=="lizard":
        if choice==("spock","paper"):
            print("Sheldon Wins")
        else:
            print("YOU WIN!!")
    elif Sheldon=="spock":
        if choice==("scissors","rock"):
            print("Sheldon Wins")
        else:
            print("YOU WIN!!")

def playagain():
    yesorno=(input("would you like to play again y/n?"))
    yesorno.lower
    if yesorno==("y"):
        return main()
    elif yesorno==("yes"):
        return main()
    else:
        print("<(^-^<) Goodbye (>^-^)>")

def main():
    getuserinfo()
    playagain()
    
main()