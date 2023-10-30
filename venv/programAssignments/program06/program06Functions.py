####################################################################
# Developer: Julian Cotto
# Date: 10/7/2023
# File Name: program06Functions.py
# Description: This file contains the functions for program06.py
####################################################################

def intro():
    print("This is Program06 - Julian Cotto")
    print("================================\n")

    print("Requirement 2\n")
    print("This program uses lists, strings, tuples, and dictionaries.\n")


def getSalesReps():
    salesReps = []
    salesRepLocations = []

    numReps = int(input("Please enter the number of sales reps to process\n"))

    for i in range(0, numReps):
        firstName = str(input("\nPlease enter the sales rep's first name\n")).capitalize()
        lastName = str(input("Please enter the sales rep's last name\n")).capitalize()
        fullName = firstName + ' ' + lastName
        salesReps.append(fullName)
        salesRepLocations.append(str(input("Please enter the rep location for: " + salesReps[i] + "\n")))

    return salesReps, salesRepLocations


def getBoatSales(salesReps, days, weeks):
    boatsSoldThursday = []
    boatsSoldFriday = []
    boatsSoldSaturday = []

    for i in range(len(weeks)):
        print("Entering Boats Sold for " + weeks[i] + "\n============================")
        for j in range(len(salesReps)):
            for k in range(len(days)):
                if days[k] == "Thursday":
                    boatsSoldThursday.append(
                        int(input("\nEnter the number of boats sold by " + salesReps[j] + " on " + days[k] + "\n")))
                elif days[k] == "Friday":
                    boatsSoldFriday.append(
                        int(input("Enter the number of boats sold by " + salesReps[j] + " on " + days[k] + "\n")))
                elif days[k] == "Saturday":
                    boatsSoldSaturday.append(
                        int(input("Enter the number of boats sold by " + salesReps[j] + " on " + days[k] + "\n")))
            print()

    return boatsSoldThursday, boatsSoldFriday, boatsSoldSaturday


def displaySalesData(weeks, salesReps, boatsSoldThursday, boatsSoldFriday, boatsSoldSaturday):
    for i in range(len(weeks)):
        print(weeks[i] + " Sales Results", "\n======================\n")
        for j in range(len(salesReps)):
            print(salesReps[j] + " Sold " + str(boatsSoldThursday[j]) + " on Thursday")
            print(salesReps[j] + " Sold " + str(boatsSoldFriday[j]) + " on Friday")
            print(salesReps[j] + " Sold " + str(boatsSoldSaturday[j]) + " on Saturday\n")


def getDealerURL(salesRepsLocations):
    dealerURLs = {}
    for i in range(len(salesRepsLocations)):
        uRL = str(input("Please Enter the Dealer URL for: " + salesRepsLocations[i] + "\n"))
        dealerURLs[i] = uRL
    return dealerURLs


def displayRepEmails(dealerURL, salesReps):
    print("Contact Sales Reps at their Emails\n==================================\n")
    for i in range(len(salesReps)):
        name = salesReps[i].split()
        email_name = "_".join(name).lower()

        print(email_name + "@" + dealerURL[i].lower() + "\n")


def experience():
    print("Program06 was a fun exercise\n"
          "I enjoyed the use of the different data forms,\n"
          "I especially enjoy passing data between functions to accomplish a goal.\n")


def outro():
    print("Thank you for running Program06 - Julian Cotto")
    input("\nPress Enter to Exit...")
