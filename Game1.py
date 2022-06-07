# Sydney Chien

# Pseudocode:
# Start
# Print Instructions
# Set list = “red, yellow, blue…..”
# Print “Hint: The word is a color”
# Choose random element
# User input “Input your guess:”
# If = then print “Sorry you missed”
# If != then print “Congratulations!” 
# Then print “Would you like to keep playing?
# If yes, loop to print instructions
# If no, end - print "Thank you for playing."

import os
import random
os.system('cls')

Game = True

for instructions in range(60): # Top border
    print("+", end = "")
print()

print("|                     GUESS THE Word                       |") # Title
print("| The randomizer will choose a random color/animal/fruit.  |") # Instructions
print("|         The object of the game is to guess that          |")
print("|          color in the least amount of chances.           |")
print("|                        Good Luck!                        |")

for instructions2 in range(60): # Bottom border
    print("+", end = "")
print()

colors = ["blue", "pink", "red", "purple", "yellow", "orange"] # Color list
animals = ["lion", "cheetah", "leopard", "puma", "tiger"] # Animal list
fruits = ["apple", "strawberry", "raspberry", "cherry", "cranberry"] # Fruit list

choice = input("Which game would you like to play? 1, 2,or 3?: ")

os.system('cls')

if choice == "1":
    while Game == True:
        print("HINT: The word is one of my FAVORITE COLORS") # Hint

        element = random.choice(colors)
        print(element," is the correct answer (for testing convenience)") # For testing

        guess = input("Input your guess:").lower() # Make sure the guess is in lower case

        if guess == element: # If =
            print("Congratulations!")
        else: # If !=
            print("Sorry, you missed.")

        again = input("Do you want to play again?:").lower()

        if again == "no":
            Game = False
            print("Thanks for playing!")
       

if choice == "2":
     while Game == True:
        print("HINT: The word is an animal in the CAT FAMILY") # Hint

        element = random.choice(animals)
        print(element," is the correct answer (for testing convenience)") # For testing

        guess = input("Input your guess:").lower() # Make sure the guess is in lower case

        if guess == element: # If =
            print("Congratulations!")
        else: # If !=
            print("Sorry, you missed.")

        again = input("Do you want to play again?:").lower()

        if again == "no":
            Game = False
            print("Thanks for playing!")

if choice == "3":
     while Game == True:
        print("HINT: The word is a RED FRUIT") # Hint

        element = random.choice(fruits)
        print(element," is the correct answer (for testing convenience)") # For testing

        guess = input("Input your guess:").lower() # Make sure the guess is in lower case

        if guess == element: # If =
            print("Congratulations!")
        else: # If !=
            print("Sorry, you missed.")

        again = input("Do you want to play again?:").lower()

        if again == "no":
            Game = False
            print("Thanks for playing!")