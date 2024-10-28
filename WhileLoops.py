### Part Two -- your code goes here. 
import random 
print("Lets play a guessing game")

secret_number = random.randint(1, 100)

def guess_number_game():
 guess = None
 while guess != secret_number:
    guess = int(input("Guess the number between 1 and 100: "))
    if guess==secret_number:
       print("correct")
    elif guess<secret_number:
        print("too low")
    elif guess>secret_number:
        print("too high")
    
guess_number_game()
