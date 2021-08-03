# Manipulate String

import datetime

now = datetime.datetime.now().year

name = input("Enter your name: ")
age = input("Enter your age: ")

dif = 100 - int(age)
hundrethyear = int(now) + int(dif) 

print("Hello, My name is " + name + ". I am " + age + " years old, and will turn 100 in the year " + str(hundrethyear) + ".") 