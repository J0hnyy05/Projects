import random


#  Uzytkownik zgaduje
def guess(x):
    random_number = random.randint(1, int(x))
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low!")
        elif guess > random_number:
            print("Sorry, guess again. Too high!")
        else:
            print("Yeah, congrats. You have guessed the number!!!")
            
user_choice = input("Choose your limit: ")
guess(user_choice)
            
        
   
   
# Komputer zgaduje  
# def computer_guess(x):
#     low = 1
#     high = int(x)
#     feedback = ''
#     while feedback != 'c':
#         if low != high:
#             guess = random.randint(low, high)
#         else:
#             guess = low
#         feedback = input(f"Is {guess} too high (H), too low (L) or correct (c)?").lower()
#         if feedback == "h":
#             high = guess - 1
#         elif feedback == "l":
#             low = guess + 1
            
#     print("Yeah, the computer has guessed your number!")
    
# number = input("Choose your limit: ")
# userNumber = input("Choose the number, which computer will have to guess: ")
# computer_guess(number)
