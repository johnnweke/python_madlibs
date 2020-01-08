# # # # print("Hello World")
# # # # print("That was easy")
# # # # print("    /|")
# # # # print("   / |")
# # # # print("  /  |")
# # # # print(" /   |")
# # # # print("/____|®")
# # #
# # # # Variables in Python
# # # # Separate different words with an underscore
# # # character_name = 'Sam'  # Variable.
# # # character_age = '29'
# # #
# # # print("There once was a man named " + character_name + ", ")
# # # print("he was " + character_age + " years old. ")
# # # print("He really liked the name " + character_name + ", ")
# # # print("but didn't like being " + character_age + ".")
# # #
# # # # Changing/Modifying Variables - define them after
# # # # Python runs from top to bottom.
# # #
# # # character_name = 'Mark'  # Variable.
# # # character_age = '45'
# # # is_male = True
# # #
# # # print("There once was a man named " + character_name + ", ")
# # # print("he was " + character_age + " years old. ")
# # # print("He really liked the name " + character_name + ", ")
# # # print("but didn't like being " + character_age + ".")
# # #
# # # # print("Celebration Media\" Empire")
# # # # # string variable
# #
# # phrase = "Celebration Media Empire"
# # print(phrase.lower())
# # print(phrase.upper().isupper())  # makes string uppercase then returns true
# #
# # # Length of a string. You know how valuable this is lol.
# # print(len(phrase))  # pass the string as a parameter inside the function len
# #
# # # How to check the value/position of something in a string
# # # First character in a string - use the print function, then the index, inside []
# #
# # print(phrase[4])
# # print(phrase[5] + phrase[8] + phrase[19])
# # print(phrase.index("E"))
# #
# # print(phrase.replace("Empire", "Studios"))
#
# # NUMBERS
# import math
#
# print(3*4.5)
# print(3+(4*5))
# print(10%3)
#
# my_number = -5
# print(str(my_number) + " is my number")
#
# # NUMBER FUNCTIONS
# print(abs(my_number))
# print(pow(my_number,3))
# print(max(my_number, -9))
#
# from math import *
#
# print(floor(3.6))
# print(ceil(3.6))
# print(sqrt(3.6))
#
# # # GETTING INPUT FROM USERS
# import datetime
# now = datetime.datetime.now()
# print(now.year)
#
# name = input("Enter your name: ")
# print("Hello " + name + "!")
# print("\nLet's find out how old you are.")
# year_born = input("What year were you born? Enter it here: ")
# user_age = now.year - int(year_born)
# print("You are " + str(user_age) + " years old.")

# # BUILDING A BASIC CALCULATOR
#
# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = float(num1) + float(num2)
# print(result)

# MADLIBS GAME
print("Roses are red")
print("Violets are blue")
print("I love you")

# create 3 variables - color, plural noun, celebrity
# store the users input inside the variables.

color = input("Enter a color: ")
plural_noun = input("Enter a Plural Noun: ")
celebrity = input("What's the name of your favorite Celebrity? ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

print("John's Madlibs!")

noun_1 = input("What's a common noun you know? ")
adjective_1 = input("What's your favorite adjective? ")




print(f"Be careful not to vacuum the {noun_1} when you clean under your bed.")
print(f"BBQ at my house! Everyone's invited, and it's Bring Your Own {noun_1}!")
print(f"If you're going to challenge a couple to a chicken fight during spring break, make sure they're more {adjective_1} than you!")
print(f"Once that {adjective_1} music comes on, it's time to shut down your acceptance speech!")













