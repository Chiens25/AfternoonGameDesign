# Sydney Chien

import os
os.system('cls')

# Even or Odd?
number = int(input("input random number:"))
remainder = number % 2 # Find remainder of 2
if remainder == 0: 
    print("even")
else: #Can only be 0(even) or 1(odd)
    print("odd")

# Multiple of 3 or 5
number2 = int(input("input random number:"))

remainder2 = number2 % 3 #Find remainder of 3
remainder3 = number2 % 5 #Find remainder of 5

if remainder2 == 0: # If no remainder then multiple of 3
    print("Multiple of 3")
else:
    print("Not a multiple of 3")
if remainder3 == 0: # If no remainder then multiple of 5
    print("Multiple of 5")
else:
    print("Not a multiple of 5")
if remainder2 == 0 and remainder3 == 0: # Practice "and" statements
    print("Multiple of both")

# Getting the last digits practice
print(number2%10) # Get the last digit
print(number2%100) # Get the last 2 digits
print(number2%1000) # Get the last 3 digits
