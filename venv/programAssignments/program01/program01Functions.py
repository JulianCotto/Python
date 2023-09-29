####################################################################
# Developer: Julian Cotto
# Date: 8/21/2023
# File Name: program01Functions.py
# Description: This file contains the functions for program01.py
####################################################################
def intro():
    print("This is Program 1 - Julian Cotto")
    print("================================")

def getInputs():
    print("Enter the following information:")
    lastName = input(str("Enter your last name:\n"))
    homeTown = input(str("Enter your hometown name:\n"))
    occupation = input(str("Enter your occupation:\n"))
    hobby = input(str("Enter your hobby:\n"))
    return lastName, homeTown, occupation, hobby

def defaultDisplay(lastName, homeTown, occupation, hobby):
    print("\nDefault Output")
    print("========================")
    print("Last Name:", lastName)
    print("Hometown:", homeTown)
    print("Occupation:", occupation)
    print("Hobby:", hobby)

def alternativeOutput(lastName, homeTown, occupation, hobby):
    print("\nAlternative Output")
    print("==================")
    print("Hello", lastName, "!\nFrom", homeTown + '.')
    print("I hope you enjoy being a(n)", occupation)
    print(hobby, "sounds like an interesting hobby.")

def moreOptions(lastName):
    counter = 1

    print("\nMore Options")
    print("============")

    print("Hello" + str(counter), lastName, '!')
    counter += 1
    print("Hello" + str(counter), lastName + '!')
    counter += 1

    for i in range(3):
        print("Hello" + str(counter), lastName + '!', end=' ')
        counter += 1

    print("\n")

def experience():
    print("\nProgram01 was a good experience.\n"
          "It was a simple warmup for the more complex work to come.\n"
          "I look forward to the rest of the semester.\n")

def outro():
    print("Thank you for running Program 1 - Julian Cotto")
    input("\nPress Enter to Exit...")
