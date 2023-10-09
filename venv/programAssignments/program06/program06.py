####################################################################
# Developer: Julian Cotto
# Date: 9/29/2023
# File Name: program05Functions.py
# Description: This file contains the functions for program05.py
####################################################################
from program06Functions import intro
from program06Functions import getSalesReps
from program06Functions import getBoatSales
from program06Functions import displaySalesData
from program06Functions import getDealerURL
from program06Functions import displayRepEmails
from program06Functions import experience
from program06Functions import outro

def main() -> None:
    weeks = ("Week One", "Week Two")
    days = ("Thursday", "Friday", "Saturday")

    print("Requirement 1\n")
    intro()
    print("Requirement 3\n")
    salesReps, salesRepsLocations = getSalesReps()
    print("\nRequirement 4\n")
    boatsSoldThursday, boatsSoldFriday, boatsSoldSaturday = getBoatSales(salesReps, days, weeks)
    print("\nRequirement 5\n")
    displaySalesData(weeks, salesReps, boatsSoldThursday, boatsSoldFriday, boatsSoldSaturday)
    print("Requirement 6\n")
    dealerURLs = getDealerURL(salesRepsLocations)
    print("\nRequirement 7\n")
    displayRepEmails(dealerURLs, salesReps)
    print("Requirement 8\n")
    experience()
    outro()


if __name__ == '__main__':
    main()