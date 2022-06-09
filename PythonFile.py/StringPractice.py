# Sydney Chien

from functools import update_wrapper
import os
os.system("cls")

print("hi")
message = "you are awesome"

print(message)
print(message[5])

length = len(message)

print(len(message))
print(message[len(message) - 1])

if message.isdigit():
    sum = message + 3
    print(sum)
else:
    print(message + " I say so")

print(message.upper())
print(message)

message = message.upper
print(message)

if message.isupper():
    print(message)
else:
    message = message.upper()
    print(message)

middle = int(length/2)
print(middle)
print(message[middle])







