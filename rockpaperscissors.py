import random

def play():
    user = input("What is your choice?: rock, paper or scissors \n")
    computer = random.choice(["rock", "paper", "scissors"])
    print(f"User chose: {user}")
    print(f"Computer chose: {computer}")
    
    if user == computer:
        return "It's a tie!!!"
    
    def isWin(player, opponent):
        if (player == "rock" and opponent == "scissors") or (player == "paper" and opponent == "rock") or (player == "scissors" and opponent == "paper"):
            return True
    
    if isWin(user, computer) == True:
        return "You won!!! \nCONGRATULATIONS!"
    
    return "You lost!!! \nTry your luck next time!"

print(play())
