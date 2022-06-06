# Daniel Walker
# from ctypes.wintypes import WORD
import random
import os 

os.system ('cls')
from time import sleep
seconds=.5

list = ["coral","scallop","sea urchin","oyster","mussel","cockle","clam","geoduck","abelone","ostrea"]
theword=random.choice(list)
print("|***************************************|")
print("|         Guess The Animal!!!           |")
print("|^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^|")
print("|          1.Instructions               |")
print("|   There are 10 animals in this game   |")
print("|     You must guess one of them        |")
print("|First we will provide you with one hint|")
print("|           !Your Hint Is!              |")
print("|  These animals are big fans of water  |")
print("|***************************************|")

guess1=input("plese put your guess here: ")
if guess1 == theword:
    print("Congrats, You got it")
else:
    print("you missed it, try again")

print("|*************************************|")
print("|         Here is a new hint          |")
print("|These creatures all have a hard shell|")
print("|        only 2 shells in fact        |")
print("|*************************************|")

guess2 = input("plese put your new guess here: ")
if guess2 == theword:
    print("Congrats, You got it")
else:
    print("wrong again, you are pretty bad at this, try again")

print("|**************************************|")
print("|       Here is your final hint        |")
print("|  These creatures almost never move   |")
print("|**************************************|")

guess3 = input("plese put your final guess here: ")

if guess3 == theword:
    print("Congrats, You got it")
else:
    print("You are horrible at guessing, no more hints, go till you get it right")

while True:
    ans = input("plese put your guess here: ")
    if ans == theword:
        name = True 
        print("Congrats, You got it")
        break 
    else:
        print("wrong again, try again")