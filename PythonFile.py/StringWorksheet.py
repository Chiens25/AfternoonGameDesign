# Sydney Chien

# 1A
from cgi import print_arguments
from pickletools import string4


str1 = "James"
print(str1)

first = 0 # Position of first letter
middle = (int(len(str1)/2)) # Position of middle letter
last = len(str1) - 1 # Position of last letter

output = str1[first] + str1[middle] + str1[last] # Combine first, middle, last letter
print(output)

# 1B
str2 = "JhonDipPeta"
print(str2)

firstA = (int(len(str2)/2)) - 1 # Position of letter before middle
middleA = (int(len(str2)/2)) # Position of middle letter
lastA = (int(len(str2)/2)) + 1 # Position of letter after middle

output2 = str2[firstA] + str2[middleA] + str2[lastA] # Combine 3 middle letters

print(output2)

str3 = "JaSonAy"
print(str3)

firstB = (int(len(str3)/2)) - 1 # Position of letter before middle
middleB = (int(len(str3)/2)) # Position of middle letter
lastB = (int(len(str3)/2)) + 1 # Position of letter after middle

output3 = str3[firstB] + str3[middleB] + str3[lastB] # Combine 3 middle letters

print(output3)

# 2 
str4 = "Ault"
str5 = "Kelly"

middleC = int(len(str4)/2) # Position of middle of "Ault"
firsthalfC = str4[0:middleC] # First half of "Ault"
secondhalfC = str4[middleC:] # Second half of "Ault"

print(firsthalfC + str5 + secondhalfC) # Combine first half, "Kelly", second half

# 3
str6 = "America"
str7 = "Japan"

middle6 = int(len(str6)/2) # Position of middle of "America"
middle7 = int(len(str7)/2) # Position of middle of "Japan"

last6 = len(str6) - 1 # Position of last letter of "America"
last7 = len(str7) - 1 # Position of last letter of "Japan"

output = str6[0] + str7[0] + str6[middle6] + str7[middle7] + str6[last6] + str7[last7]
print(output) # Combine first letters, middle letters, last letters

# 4
str8 = "PyNaTive"

if str8[0].islower(): # If letter is lowercase then print
    print(str8[0], end="") # End= gets rid of space between letters
if str8[1].islower():
    print(str8[1], end="")
if str8[2].islower():
    print(str8[2], end="")
if str8[3].islower():
    print(str8[3], end="")
if str8[4].islower():
    print(str8[4], end="")
if str8[5].islower():
    print(str8[5], end="")
if str8[6].islower():
    print(str8[6], end="")
if str8[7].islower():
    print(str8[7], end="")


if str8[0].isupper(): # If letter is uppercase then print
    print(str8[0], end="")
if str8[1].isupper():
    print(str8[1], end="")
if str8[2].isupper():
    print(str8[2], end="")
if str8[3].isupper():
    print(str8[3], end="")
if str8[4].isupper():
    print(str8[4], end="")
if str8[5].isupper():
    print(str8[5], end="")
if str8[6].isupper():
    print(str8[6], end="")
if str8[7].isupper():
    print(str8[7], end="")








