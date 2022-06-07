# Sydney Chien
# Program about using files, date, time
# r = read
# a = append
# w = write 
# Goal: Saving scores

import random
import os, datetime

os.system('cls')

date = datetime.datetime.now() # date and time now
print(date) # year, month, date, time
print(date.strftime("%m / %d / %Y"))
print(type(date.strftime("%m / %d / %Y")))

name = "Sydney"
sce = 344
scrLine = str(sce) + "\t\t" + name + "\t" + date.strftime("%m / %d / %Y"") + "\t"
print(scrLine)

# Create a file
myFile = open("scre.txt") # creates a new file for you
myFile.write(scrLine)
myFile.close()

# Create new line
name = "Peter"
sce = 132
scrLine = str(sce) + "\t\t" + name + "\t" + date.strftime("%m / %d / %Y"") + "\n"

# Append tyr file add lines the file
myFile = open("scre.txt", 'a')
myFile.write(scrLine)
myFile.close()

# Read the file
myFile = open("scre.txt", 'r')
stuff = myFile.readline()
myFile.close()
print(stuff)


