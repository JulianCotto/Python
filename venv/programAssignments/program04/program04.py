####################################################################
# Developer: Julian Cotto
# Date: 9/18/2023
# File Name: program04Functions.py
# Description: This file contains the functions for program04.py
####################################################################
from program04Functions import intro
from program04Functions import musicPref
from program04Functions import collectData
from program04Functions import membershipLvl
from program04Functions import seatAssign
from program04Functions import filterCustomerData
from program04Functions import customerSurvey
from program04Functions import experience
from program04Functions import outro

def main() -> None:
    customerData = {}
    print("Requirement 1\n")
    intro()
    print("Requirement 3\n")
    genre = musicPref(customerData)
    if genre == "classical":
        print("Requirement 4\n")
        customerData = collectData(customerData)
        customerData = membershipLvl(customerData)
        customerData = seatAssign(customerData)
        print("Requirement 5\n")
        filterCustomerData(customerData)
        print("Requirement 6\n")
        print("Thank you for attending the concert")
        customerSurvey(customerData)
        experience()
    else:
        print("We do not recognize the", genre, "musical genre. Sorry.")
    outro()


if __name__ == '__main__':
    main()