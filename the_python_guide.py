# Chapter 23(Modules)

import basic_operations
import math as m

print(m.e)
print(m.sqrt(121))
print(basic_operations.add(5, 4))

# Chapter 25(Files)

people_file = open("people.txt", "w")
people_file.write("John\n")
people_file.write("Bob\n")
people_file.write("Jane\n")
people_file.close()

people_file = open("people.txt", "a")
people_file.write("Sarah\n")
people_file.write("John\n")
people_file.write("Jane\n")
people_file.close()

people_file = open("people.txt", "r")
for line in people_file:
    print(line)
people_file.close()

import shutil
import os

if os.path.exists("people.txt"):
    shutil.copyfile("people.txt", "new_people.txt")
    os.remove("people.txt")
else:
    print("File does not exist")

if os.path.exists("new_people.txt"):
    shutil.move('new_people.txt', 'people.txt')

# Chapter 28(Exceptions)

try:
    32/0
except ZeroDivisionError:
    print("Division by zero")
else:
    print("No ZeroDivisionError")
finally:
    print("Finally block")
