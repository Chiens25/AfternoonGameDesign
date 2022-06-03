import os
os.system('cls')

# Even or Odd?
number = int(input("input random number:"))
remainder = number % 2
if remainder == 0:
    print("even")
if remainder == 1:
    print("odd")

# Multiple of 3 or 5
number2 = int(input("input random number:"))

remainder2 = number2 % 3
remainder3 = number2 % 5

if remainder2 == 0:
    print("Multiple of 3")
else:
    print("not a multiple of 3")
if remainder3 == 0:
    print("Multiple of 5")
else:
    print("not a multiple of 5")