####################################################################
# Developer: Julian Cotto
# Date: 9/29/2023
# File Name: program05Functions.py
# Description: This file contains the functions for program05.py
####################################################################
from program05Functions import intro
from program05Functions import getNumAuthors
from program05Functions import getAuthorDetails
from program05Functions import getAuthorBookDetails
from program05Functions import displayObject
from program05Functions import experience
from program05Functions import outro

def main() -> None:
    authorObject = {}
    counter = 0

    print("Requirement 1\n")
    intro()
    print("Requirement 3\n")
    numAuthors = getNumAuthors()
    print("Requirement 4\n")
    for i in range(0, numAuthors):
        authorObject[i] = {}
        authorObject[i]['authorName'], \
        authorObject[i]['authorURL'] = getAuthorDetails()
    print("Requirement 5\n")
    for key in authorObject:
        authorObject[key]['book_name_list'], \
        authorObject[key]['book_isbn_list'], \
        authorObject[key]['book_order_quantity_list'], counter = getAuthorBookDetails(authorObject, counter)
        counter += 1
    print("\nRequirement 6 & 7\n")
    displayObject(authorObject)
    print("Requirement 8\n")
    experience()
    outro()

if __name__ == '__main__':
    main()
