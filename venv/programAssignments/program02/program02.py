####################################################################
# Developer: Julian Cotto
# Date: 8/28/2023
# File Name: program02.py
# Description: This file contains the main function for
# program02.py:
####################################################################
from program02Functions import intro
from program02Functions import programPurpose
from program02Functions import salesInput
from program02Functions import getSales
from program02Functions import moreSales
from program02Functions import getTotal
from program02Functions import moreSalesLoop
from program02Functions import experience
def main() -> None:
    accumulator = 0.00
    cont = 'y'
    print("Requirement 1\n")
    intro()
    print("Requirement 2\n")
    programPurpose()
    print("Requirement 3\n")
    salesResponse = salesInput()
    print("Requirement 4\n")
    accumulator += getSales(salesResponse)
    print("Requirement 5\n")
    getTotal(accumulator)
    print("Requirement 6\n")
    while cont == 'y':
        cont, accumulator = moreSalesLoop(cont, accumulator)
    print("Requirement 7\n")
    getTotal(accumulator)
    print("Requirement 8\n")
    experience()

if __name__ == '__main__':
    main()