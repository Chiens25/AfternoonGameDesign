# Sydney Chien

from ctypes.wintypes import WORD
import random
import os, datetime

os.system ('cls')
from time import sleep
seconds=.5

theWord=""

colors = ["blue", "pink", "red", "purple", "yellow", "orange"] # Color list
animals = ["lion", "cheetah", "leopard", "puma", "tiger"] # Animal list
fruits = ["apple", "strawberry", "raspberry", "cherry", "cranberry"] # Fruit list

Game=True
cnt=0
#a function is a section  the prram that we call when we need it
def scoreboard():
    global cnt     #allow us to modify the variable all over the program
    if cnt ==0 and choice == 1:
         print("HINT: The word is one of my FAVORITE COLORS") 
    if cnt ==0 and choice == 2:
        print("HINT: The word is an animal in the CAT FAMILY") # Hint
    if cnt ==0 and choice == 3:
        print("HINT: The word is a RED FRUIT") # Hint
    elif cnt !=0:
        print("Not quite... Try again!")

    print()
def selectWrd(choice):  #is a function with a parameter
    global theWord
    if choice ==1:
        theWord= random.choice(colors)    
    if choice ==2:
        theWord= random.choice(animals)
    if choice ==3:
        theWord= random.choice(fruits)
    return theWord  
name=input("What is your name?: ")
high=0 #tfind highest score

while Game:
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


    print(name, end=", ")
    answer=input("Would you like to play?: ")
    if 'n' in answer:
        break
    while True:
        choice=input("Which game would you like to play 1, 2, or 3?: ")
        #preventing error we use try and except
        try:
            choice=int(choice)
            if choice>0 and choice <4:
                break
            else:
                print("give me 1,2  3")
        except:
            print("sorry")
    theWord = selectWrd(choice) #call to a function that will return a value
    #call function to select the word from the right list
    os.system('cls')
    check=True
    while check and cnt <5:
        guess=input("Plese put your guess here: ")
        print()
        if guess == theWord:
            print("Congrats, You got it!")
            check=False
        else:
            scoreboard()
        cnt+=1   # cnt= cnt - 1
        if cnt ==5:
            print("Sorry!" )
    score=200-40*cnt
    if score > high:   # find highest sce
        high=score
    print(name+", your score is "+str(score))
    input("Press enter ")
    os.system('cls')
    print("<><><><><><><><><><><><>")
    answer=input("Do yo want to play again? ")
    if ('n' or 'N') in answer:
        Game=False
        print("Thank you for playing my game" )
    
    cnt=0 
    print("your highest score is " + str(high))
    date = datetime.datetime.now()
    scrLine=str(score)+"\t "+ name + "\t"+date.strftime("%m-%d-%Y")+ "\n"
    myFile = open("G2.txt", 'w')
    myFile.write(scrLine)
    myFile.close()
    #Append tyr file add lines tthe file
    myFile = open("G2.txt", 'a')
    myFile.write(scrLine)
    myFile.close()
    #REad the file
    myFile = open("G2.txt", 'r')
    stuff=myFile.readlines()
    myFile.close()
    for line in stuff:
        print(line)


