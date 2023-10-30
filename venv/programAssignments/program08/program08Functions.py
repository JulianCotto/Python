####################################################################
# Developer: Julian Cotto
# Date: 10/27/2023
# File Name: program08Functions.py
# Description: This file contains the functions for program08.py
####################################################################

class Pokemon:
    def __init__(self, name, ability):
        self.__name = name
        self.__ability = ability

    def get_name(self):
        return self.__name

    def get_ability(self):
        return self.__ability


def getRequirementNum(num):
    if num == 1:
        print("Requirement 1\n")
    elif num == 2:
        print("Requirement 2\n")
    elif num == 3:
        print("Requirement 3 & 4\n")
    elif num == 4:
        print("\nRequirement 5\n")
    else:
        print("Requirement 6\n")


def intro():
    print("This is Program08 - Julian Cotto")
    print("================================\n")


def getProgPurpose():
    print("This program keeps track of Pokémon characters.\n")


def addPokedexEntry():
    pokedex = []
    moreEntries = True

    while moreEntries:
        answer = input("Do you have a pokemon to enter? (y/n)\n")
        if answer.lower() == 'n':
            moreEntries = False
        else:
            name = input("Enter name for pokemon #{} \n".format(len(pokedex) + 1))
            ability = input("Enter Ability for pokemon #{} \n".format(len(pokedex) + 1, '\n'))
            pokedex.append(Pokemon(name, ability))

    return pokedex


def getPokedexEntries(pokedex):
    for i, pokemon in enumerate(pokedex, start=1):
        print("Name of pokemon #{}: {}".format(i, pokemon.get_name()))
        print("Ability of pokemon #{}: {}".format(i, pokemon.get_ability()), '\n')


def experience():
    print("Abstracting and creating classes is probably my favorite activity.\n"
          "I also very much enjoy playing Pokemon Go on my cell phone.\n"
          "This was a simple class to build that incorporates 2 of my favorite activities\n")


def outro():
    print("Thank you for running Program08 - Julian Cotto")
    input("\nPress Enter to Exit...")
