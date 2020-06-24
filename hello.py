# This is how you comment a line of text
# import os
# os.system('osascript send.scpt {} "{}"'.format(7188134058, "hi"))
"""
This is how you comment a block of text
"""
from math import *  # math is called a module

def string_input():
    age = 3.14159
    name = input("Enter your name: ") # Getting input from user
    age = input("Enter your age: ") # age is default a string
    # Note: age is overwritten even though they are different types
    print("Hello World!\n")
    print("My name is \""+name.upper()+"\" and I am "+age)
    print(name[0]+name[1]+name[2]+name[3] + " is " + str(len(name)) + " letters long")

    # This code replaces "ene" in "Gene" with "GElephantelephant" and then returns the index of "lephant" after the 5th index
    print(name.replace("ene","Elephantelephant").index("lephant",5))

    print(age + " something") # age is a string
    num = round(max(pow(abs(-int(age)%3),5),20.1231),3)
    print(num) # age is an int
    print(floor(num))
    print(int(sqrt(num)))
    print(sqrt(num))

# list
def friends():
    friends = ["Claudia", "Sam", "Jake", "Ashleigh",234]
    print(friends[-2][3]) # negative index starts from back
    print(friends[0:3]) # index from 0 to 2 (NOT INCLUDING 3)
    friends[-2] = "Jeter"
    print(friends)
    friends.extend(["Kevin","Daniel","Brian"])
    friends.append("Chis")
    friends.insert(0,"Kevin") # inserts Kevin in front of list instead of back
    friends.remove("Chis")
    friends.pop()
    print(friends.index("Kevin"))
    print(friends.count("Kevin"))
    # .sort() and .reverse() is for sorting/reversing numbers
    friends2 = friends.copy()
    print(friends2)

    # tuples
    # diff between lists and tuples. tuples are immutable - cannot be changed, will get error
    coordinates = (4,5)
    print(coordinates[1])

name="Gene"
age = 20
def say_hi(name,age):
    print("Hello "+name+","+str(age))
def cube(num):
    if (num<-50) or (num>50):
        return "the num is too large"
    elif num==0 and num!=50:
        return 0
    else:
        return num*num*num
# print(cube(51)) # without return statement, you get "None"
# print(cube(-1))
# print(cube(0))


