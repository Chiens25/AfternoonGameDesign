# Sydney Chien

import os
os.system('cls')

yearborn = int(input("input the year you were born: "))
currentyear = 2022 
age = currentyear - yearborn # Subtract year born from current year to find age
print ("you are", age)

if(age < 50): # Less than statemant 
    print("you are young")

if(age > 50): # Greater than statement
    print("you are old")

if(age == 50): # Equal to statement
    print("you are blah")




