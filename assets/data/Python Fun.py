import random # Package loaded in so I can use the random number generator

print("Hello. Welcome to my minigame!")

# Variables for the start of the game that store your upper and lower bounds
low = int(input("Enter Lower Bound:"))
high = int(input("Enter Higher Bound:"))

# f seems to allow you to insert variables and \n creates a new space
print(f"\n You have 5 chances to guess the number between {low} and {high}. Begin!")

num = random.randint(low,high) # Picks random number between the low and high bounds
ch = 5                         # Amount of guesses you have
gc = 0                         # Guess Counter

# Use a while loop to create game
while gc < ch:
    gc += 1
    guess = int(input("Insert your guess: "))

    if guess == num: # If you guess the correct number
        print("Congradulations, you win!")
        
        break
    elif gc >= ch and guess != num: # If you did not get the right number
        print("Sorry! You ran out of guesses.")
        print(f"The correct number was {num}. ") # Prints out the correct number so you know how close you were

    elif guess < num: # Guessed too low
        print("Wrong Number! Too low!")


    elif guess > num: # Guessed too high
        print("Wrong Number! Too High!")
    





