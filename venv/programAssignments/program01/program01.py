####################################################################
# Developer: Julian Cotto
# Date: 8/21/2023
# File Name: program01.py
# Description: This file contains the main function for program01.py
####################################################################
from program01Functions import intro
from program01Functions import getInputs
from program01Functions import defaultDisplay
from program01Functions import alternativeOutput
from program01Functions import moreOptions
from program01Functions import outro
from program01Functions import experience

def main() -> None:
    print("Requirement 1\n")
    intro()
    print("\nRequirement 2\n")
    lastName, homeTown, occupation, hobby = getInputs()
    print("\nRequirement 3")
    defaultDisplay(lastName, homeTown, occupation, hobby)
    print("\nRequirement 4")
    alternativeOutput(lastName, homeTown, occupation, hobby)
    print("\nRequirement 5")
    moreOptions(lastName)
    print("Requirement 6")
    experience()
    outro()

if __name__ == '__main__':
    main()