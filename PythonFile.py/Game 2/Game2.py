# Sydney Chien
# Number Guessing Game

# *PROBLEM* - WORKS ON THE FIRST RUN AND THEN GOES STRAIGHT TO CHOICE 5

import os, datetime # Import date and time
import random # Import random function
os.system('cls')

# Define variables
high = 0 
number = 0
Game = True
count = 0

def instructions():
    myFile = open("instructions.txt", 'r')
    content = myFile.readlines()
    for lines in content:
        print(lines)
    myFile.close()


def hint(): # Define hint
    global count     
    if count == 0 and choice == 2: # After first try on 1-25
        remainder = number % 2
        if remainder == 0: # If remainder is zero/one then it is an even/odd number
                print("HINT: The number is EVEN")
        else: 
                print("HINT: The number is ODD")
    if count == 0 and choice == 3: # After first try on 1-50
        remainder = number % 2
        if remainder == 0: # If remainder is zero/one then it is an even/odd number
                print("HINT: The number is EVEN")
        else: 
                print("HINT: The number is ODD")
    if count == 0 and choice == 4: # After first try on 1-100
        remainder = number % 2
        if remainder == 0: # If remainder is zero/one then it is an even/odd number
                print("HINT: The number is EVEN")
        else: 
                print("HINT: The number is ODD")
    elif count == 0 or count < 4: # For guesses 1-5 tells user if guess is too high/low 
        if guess > number:
            print("Too high!")
        if guess < number:
            print("Too low!")


    print()

def randomNumber(choice):  
    global number
    if choice == 2:
        number = random.randint(1, 25) # Random number generator
    if choice == 3:
         number = random.randint(1, 50) # Random number generator
    if choice == 4:
         number = random.randint(1, 100) # Random number generator
    return number  

name = input("What is your name?: ") # Input name for scoreboard
high = 0 # Define high

while Game: 
    for menu in range(56): # Top border
        print("+", end = "")
    print()
    print("|                    NUMBER GAME                       |") # Main menu
    print("|                 1. Instructions                      |") 
    print("|                 2. Play Level 1-25                   |")
    print("|                 3. Play Level 1-50                   |")
    print("|                 4. Play Level 1-100                  |")
    print("|                 5. Print Score                       |")
    print("|                 6. Exit                              |")

    for menu in range(56): # Bottom border
        print("+", end = "")
    print()
    choice = input("Select option 1-6: ") # User input option choice
    while True:
        try: # Accounts for non 1-7 inputs
            choice=int(choice) # Make it an integer so you dont have to go through with "" plus it adds value
            if choice>0 and choice <7: 
                break
            else:
                print("give me 1-7")
        except:
            print("sorry")
    if choice > 1 or choice < 5:
        number = randomNumber(choice) # Set number to random number
        check = True


    if choice == 1: # Print the instructions
        instructions()
        input("Press enter: ")
        check = False

    if choice == 5: # Print the scoresheet
        myFile = open("PythonFile.py\Game 2\G2score.txt", 'r')
        stuff = myFile.readlines()
        myFile.close()
        stuff.sort(reverse = True) # Puts largest digit on the top
        for line in stuff:
            print(line)
        input("Press enter: ")
        check = False

    if choice == 6:
        
        print("Thanks for playing!", high)
        if high > 50:
            myFile = open("Game 2\G2score.txt", 'a')
            date=datetime.datetime.now()
            scrLine = str(high)+"\t "+ name + "\t"+ date.strftime("%m-%d-%Y")+ "\n"
            myFile.write(scrLine)
            myFile.close()
        break
        os.system('cls')
    
    while check and count < 5:
        guess = int(input("Plese put your guess here: "))
        print()
        if guess == number:
            print("Congrats, You got it!")
            check=False
        else:
            hint()
        count+=1   
        if count ==5:
            print("Sorry! The number was", number )
    if check or count ==5:
        score = 800-40*count
        if score > high:   
            high=score
        print(name +", your score is "+str(score))
        input("Press enter: ")
        os.system('cls')
print(high)





