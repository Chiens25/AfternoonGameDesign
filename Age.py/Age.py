import os
os.system('cls')

yearborn = int(input("input the year you were born: "))
currentyear = 2022
age = currentyear - yearborn
print (age)

if(age < 50):
    print("you are young")

if(age > 50):
    print("you are old")

if(age == 50):
    print("you are blah")




