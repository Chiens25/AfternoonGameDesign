# Sydney Chien

# Lists, list functions and methods, add elements, delete elements
# For loops
# Random class

import os
import random
os.system('cls')

# A list is an array, is indexed, is changeable

myList = [1,2,3,4,5]
#         0,1,2,3,
print(myList)
print(myList[1]) # print element in position 1
print(myList[1:3]) # print element in position 1,2
print(myList[-1]) # print the last element
print(myList[-3:]) # print the last 3 elements

myFruits = ["apple", "banana", "kiwi", "papaya", "pear"]
print(myFruits[:3]) # print element 1,2,3
lengthList = len(myFruits) # Number of elements is always one less than your last index
print(lengthList)
print(myFruits[lengthList - 1])
print(myFruits[0])

#For loop repeats specific
for elem in myFruits: # Control the loop
    print(elem)
for elem in range(lengthList):
    print(elem, end="=")
    print(myFruits[elem])

if "apple" in myFruits:
    print("Apple is in the list")

# Add to lists
myFruits.append("guava") # Append only adds elements
print(myFruits)

myFruits.insert(2, "orange") # Insert index where you want element to go
print(myFruits)

print(myList)
myList.extend(myFruits)
print(myList)

myList = [1,2,3,4,5]
print(myList)
myList.append(myFruits) # List inside of a list
print(myList) 
print(myList[5])
print(myList[5][1])

myFruits[1] = "cherry" # Replace position 2 (banana)
print(myFruits)

# Random
for i in range(5):
    element = random.choice(myFruits)
    print(element, end = " ")

element = random.choice(myFruits)
print(element)
