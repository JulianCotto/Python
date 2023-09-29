####################################################################
# Developer: Julian Cotto
# Date: 8/28/2023
# File Name: program02.py
# Description: This file contains the main function for program02.py
####################################################################
def intro():
    print("This is Program 2 - Julian Cotto")
    print("================================\n")

def programPurpose():
    print("This program calculates strawberry sales for the month.\n")

def salesInput():
    sales = input("Do you have sales to input? (Y/N)\n")
    while sales.lower() != 'y' and sales.lower() != 'n':
        sales = input("Invalid input. Please enter Y or N.\n")
    return sales

def getSales(salesResponse):
    if salesResponse.lower() == 'y':
        sales = float(input("Enter sales to add them to the accumulator.\n"))
    else:
        sales = 0.00
    return sales

def moreSales(accumulator):
    moreSales = getSales(retSales)
    accumulator += moreSales
    return moreSales

def getTotal(accumulator):
    sales = format(accumulator, '.2f')
    print("The total strawberry sales are: $" + sales, '\n')

def moreSalesLoop(cont, accumulator):
    cont = input("Do you have additional sales to add to the accumulator? (Y/N)\n")
    while cont.lower() != 'y' and cont.lower() != 'n':
        cont = input("Invalid input. Please enter Y or N.\n")
    if cont.lower() == 'y':
        accumulator += getSales(cont)
        getTotal(accumulator)
    else:
        cont = 'n'
    return cont, accumulator

def experience():
    print("\nProgram02 was mildly more challenging.\n"
          "It was still simple overall an I enjoyed it.\n"
          "I Love the structured approach python takes in its coding.\n")