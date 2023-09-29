####################################################################
# Developer: Julian Cotto
# Date: 9/29/2023
# File Name: program05Functions.py
# Description: This file contains the functions for program05.py
####################################################################
from program05Functions import intro
from program05Functions import getNumAuthors
from program05Functions import getAuthorInfo

def main() -> None:
    # object to be filled during program execution and displayed at the end
    displayObject = {}
    continueLoop = 0

    print("Requirement 1\n")
    intro()
    print("Requirement 3\n")
    numAuthors = getNumAuthors()
    print("Requirement 4\n")
    while continueLoop != -1:
        displayObject = getAuthorInfo(displayObject, numAuthors)
        continueLoop = int(input("Enter -1 to exit or any other number to continue\n"))



if __name__ == '__main__':
    main()