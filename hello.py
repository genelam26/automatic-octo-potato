# This is how you comment a line of text
# import os
# os.system('osascript send.scpt {} "{}"'.format(number, "message"))
"""
This is how you comment a block of text
"""
from math import *  # math is called a module
import random
from Student import Student # from (file) import (class)
from Teacher import Teacher

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

# Dictionaries
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "April": "April",
    5: "May",
    6: "June",
}
# print(monthConversions["Jan"])
# print(monthConversions.get(6))
# print(monthConversions.get(7))

# Loops
def whileLoop():
    i=0
    while i<50:
        print(i)
        i+=1
    print("Done with while loop")
def forLoop():
    for letter in "Giraffe Academy":
        print(letter)
    friends=["Kim","Karen","Jim"]
    for friend in friends:
        print(friend)
    i=10
    for j in range(2,i,2):
        print(j)
    for index in range(len(friends)):
        print(index, friends[index])
    print("Done with for loop")
# whileLoop()
# forLoop()
def power(base,pow_num):
    power=1
    for i in range(pow_num):
        power*=base
    return power
#print(power(2,7))

def grid():
    number_grid = [[1,2,3],[4,5,6,],[7,8,9],[0]]
    print(number_grid[3][0]) # may get index of bounds error
    for row in number_grid:
        for column in row:
            print(column)
    print("done")
# grid()
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": # or letter.lower() in "aeiou"
            translation=translation+"g"
        else:
            translation = translation + letter
    return translation
# print(translate(input("Enter a phrase")))

def trycatch():
    try:
        number=int(input("Enter an integer "))
        second=int(input("Enter another num "))
        print(number/second)
    except ZeroDivisionError as err: # bad practice to have general except: statement.
        print(err)
    except ValueError:
        print("invalid error")
# trycatch()
def fileHandling():
    path="/Users/genelam/Downloads/copy.txt"
    file = open(path,"r+")
    print(file.readable())
    print(file.writable())
    #print(file.readlines()) # takes each line and adds it to a list
    #print(file.readline())
    for line in file.readlines():
        print(line)
    file.write("\n something")
    for line in file.readlines():
        print(line)
    secondfile = open("index.html","w+") #creates index.html
    secondfile.write("something")
    secondfile.read()
    file.read()
    file.close()
    secondfile.close()
# fileHandling()

# Objects and Inheritance
student1=Student("Selena","Computer Science and Sociology",4.0,True)
print(student1.to_String())
student1.pay_Tuition()
teacher1=Teacher("Gene","Computer Engineering",4.0,False)
print(teacher1.to_String())
teacher1.pay_Tuition()
