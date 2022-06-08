# Sydney Chien
# Number Guessing Game

import os, datetime 
import random
os.system('cls')

high = 0

Game = True
count = 0


def scoreboard():
    global count     
    if count == 0 and choice == 2:
        remainder = number % 2
        if remainder == 0: 
                print("HINT: The number is EVEN")
        else: 
                print("HINT: The number is ODD")
    if count ==0 and choice == 3:
        remainder = number % 2
        if remainder == 0: 
                print("HINT: The number is EVEN")
        else: 
                print("HINT: The number is ODD")
    if count ==0 and choice == 4:
        remainder = number % 2
        if remainder == 0: 
                print("HINT: The number is EVEN")
        else: 
                print("HINT: The number is ODD")
    elif count != 0 and count < 4:
        if guess > number:
            print("Too high!")
        if guess < number:
            print("Too low!")


    print()

def randomNumber(choice):  
    global number
    if choice == 2:
        number = random.randint(1, 25)  
    if choice == 3:
         number = random.randint(1, 50)
    if choice == 4:
         number = random.randint(1, 100)
    return number  

name = input("What is your name?: ")
high = 0 

while Game:
    for menu in range(60): # Top border
        print("+", end = "")
    print()
    print("|                    NUMBER GAME                       |") # Title
    print("|                 1. Instructions                      |") 
    print("|                 2. Play Level 1-25                   |")
    print("|                 3. Play Level 1-50                   |")
    print("|                 4. Play Level 1-100                  |")
    print("|                 5. Print Score                       |")
    print("|                 6. Exit                              |")

    for menu in range(60): # Bottom border
        print("+", end = "")
    print()
    choice = (input("Select option 1-6: "))

    number = randomNumber(choice) 
    os.system('cls')
    check = True
    while check and count <5:
        guess = input("Plese put your guess here: ")
        print()
        if guess == number:
            print("Congrats, You got it!")
            check=False
        else:
            scoreboard()
        count+=1   
        if count ==5:
            print("Sorry!" )
    score = 200-40*count
    if score > high:   
        high=score
    print(name +", your score is "+str(score))
    input("Press enter: ")

if choice == 1:
    myFile = open("G2.txt", 'r')
    content = myFile.readlines()
    for line in content:
        print(line)
    myFile.close()

if choice == 4:
    myFile = open("G2score.txt", 'r')
    stuff = myFile.readlines()
    myFile.close()
    stuff.sort(reverse = True)
    for line in stuff:
        print(line)

if choice == 5:
    print("Thanks for playing!")




