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

for instructions in range(60): # Top border
    print("+", end = "")
print()

print("|                     GUESS THE COLOR                      |") # Title
print("|        The randomizer will choose a random color.        |") # Instructions
print("|         The object of the game is to guess that          |")
print("|          color in the least amount of chances.           |")
print("|                        Good Luck!                        |")

colors = ["blue", "pink", "red", "purple", "yellow", "orange"] # Color list

for instructions2 in range(60): # Bottom border
    print("+", end = "")
print()

print("HINT: The word is one of my FAVORITE COLORS") # Hint

element = random.choice(colors)
print(element," is the correct answer (for testing convenience)") # For testing

guess = input("Input your guess:").lower()

if guess == element:
    print("Congratulations!")
else:
    print("Sorry you missed.")







