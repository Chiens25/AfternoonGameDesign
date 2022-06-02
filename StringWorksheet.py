# 1A
from cgi import print_arguments
from pickletools import string4


str1 = "James"
print(str1)

first = 0
middle = (int(len(str1)/2))
last = len(str1) - 1

output = str1[first] + str1[middle] + str1[last]
print(output)

# 1B
str2 = "JhonDipPeta"
print(str2)

firstA = (int(len(str2)/2)) - 1
middleA = (int(len(str2)/2))
lastA = (int(len(str2)/2)) + 1

output2 = str2[firstA] + str2[middleA] + str2[lastA]

print(output2)

str3 = "JaSonAy"
print(str3)

firstB = (int(len(str3)/2)) - 1
middleB = (int(len(str3)/2)) 
lastB = (int(len(str3)/2)) + 1

output3 = str3[firstB] + str3[middleB] + str3[lastB]

print(output3)

# 2 
str4 = "Ault"
str5 = "Kelly"

middleC = int(len(str4)/2)
firsthalfC = str4[0:middleC]
secondhalfC = str4[middleC:]

print(firsthalfC + str5 + secondhalfC)

# 3
str6 = "America"
str7 = "Japan"

middle6 = int(len(str6)/2)
middle7 = int(len(str7)/2)

first6 = 0

last6 = len(str6) - 1
last7 = len(str7) - 1

output = str6[0] + str7[0] + str6[middle6] + str7[middle7] + str6[last6] + str7[last7]
print(output)

# 4
str8 = "PyNaTive"

if str8[0].islower():
    print(str8[0])
if str8[1].islower():
    print(str8[1])
if str8[2].islower():
    print(str8[2])
if str8[3].islower():
    print(str8[3])
if str8[4].islower():
    print(str8[4])
if str8[5].islower():
    print(str8[5])
if str8[6].islower():
    print(str8[6])
if str8[7].islower():
    print(str8[7])
if str8[8].islower():
    print(str8[8])

if str8[0].isupper():
    print(str8[0])
if str8[1].isupper():
    print(str8[1])
if str8[2].isupper():
    print(str8[2])
if str8[3].isupper():
    print(str8[3])
if str8[4].isupper():
    print(str8[4])
if str8[5].isupper():
    print(str8[5])
if str8[6].isupper():
    print(str8[6])
if str8[7].isupper():
    print(str8[7])
if str8[8].isupper():
    print(str8[8])








