####################################################################
# Developer: Julian Cotto
# Date: 9/29/2023
# File Name: program05Functions.py
# Description: This file contains the functions for program05.py
####################################################################

def intro():
    print("This is Program04 - Julian Cotto")
    print("================================\n")

    print("Requirement 2\n")
    print("This program records Book People product data.\n")


def getNumAuthors():
    numAuthors = int(input("Please enter the number of authors to process\n"))
    return numAuthors


def getAuthorDetails():
    authorName = str(input("Enter Author Name\n"))
    authorSite = input("Enter Author Website URL\n")
    return authorName, authorSite


def getAuthorBookDetails(authorObject, counter):
    continueLoop = 0
    book_name_list, book_isbn_list, book_order_quantity_list = [], [], []

    while continueLoop != '-1':
        bookName = str(input("Enter a Book Written by " + authorObject[counter]['authorName']))
        book_name_list.append(bookName)

        bookISBN = str(input("Enter the Book ISBN for " + bookName))
        book_isbn_list.append(bookISBN)

        orderQuantity = int(input("How many copies of " + bookName + " would you like to order?"))
        book_order_quantity_list.append(orderQuantity)

        continueLoop = str(input("Enter more books by " + authorObject[counter]['authorName']))

    return book_name_list, book_isbn_list, book_order_quantity_list, counter
