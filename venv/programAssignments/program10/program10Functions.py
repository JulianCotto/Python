####################################################################
"""
Developer: Julian Cotto
Date: 11/12/2023
File Name: program10.py
Description: This file contains the main function for program10.py
"""
####################################################################
import pyperclip
import re
import pyinputplus as pyip


def getRequirementNum(num):
    if num == 1:
        print("Requirement 1\n")
    elif num == 2:
        print("Requirement 2\n")
    elif num == 3:
        print("Requirement 3\n")
    elif num == 4:
        print("Requirement 4\n")
    elif num == 5:
        print("Requirement 5\n")
    elif num == 6:
        print("Requirement 6\n")
    elif num == 7:
        print("Requirement 7\n")
    elif num == 8:
        print("Requirement 8\n")
    elif num == 9:
        print("\nRequirement 9\n")
    elif num == 10:
        print("Requirement 10\n")
    elif num == 11:
        print("Requirement 11\n")
    elif num == 12:
        print("\nRequirement 12\n")
    elif num == 13:
        print("\nRequirement 13\n")
    elif num == 14:
        print("\nRequirement 14\n")
    elif num == 15:
        print("\nRequirement 15")
    elif num == 16:
        print("Requirement 16\n")
    elif num == 17:
        print("\nRequirement 17\n")
    elif num == 18:
        print("\nRequirement 18\n")
    elif num == 19:
        print("\nRequirement 19\n")
    elif num == 20:
        print("\nRequirement 20\n")
    elif num == 21:
        print("\nRequirement 21\n")
    elif num == 22:
        print("\nRequirement 22\n")
    elif num == 23:
        print("\nRequirement 23\n")
    elif num == 24:
        print("\nRequirement 24\n")
    else:
        print("\nRequirement 25\n")


def intro():
    print("This is Program10 - Julian Cotto")
    print("================================\n")


def getProgPurpose():
    print("This program works with strings, uses regular expressions, and performs input validation tasks.”\n")


def displayEscapeChars():
    print("These are the 5 Python Escape Characters in a String\n",
          "Single Quote: (\\')\n",
          "Double Quote: (\\\")\n",
          "Tab Space: (\\t)\n",
          "Newline: (\\n)\n",
          "Backslash: (\\\)\n")


def displayEscapeCharsRaw():
    print(r"These are the 5 Python Escape Characters in a Raw String", '\n',
          r"Single Quote: (\')", '\n',
          r"Double Quote: (\")", '\n',
          r"Tab Space: (\t)", '\n',
          r"Newline: (\n)", '\n',
          r"Backslash: (\\)", '\n')


def singleTripleQuotes():
    multiLineString = '''
    This is a multiline string.
    This multiline string uses single quotes
    to create the string on multiple lines
    '''
    print(multiLineString)


def doubleTripleQuotes():
    multiLineString = """
    This is a multiline string.
    This multiline string uses double quotes
    to create the string on multiple lines
    """
    print(multiLineString)


def indexedCharacters():
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    return alphabet[0], alphabet[-6], alphabet[3:], alphabet[:7]


def inAndNotOps():
    checkList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if 1 in checkList:
        print("1 is in the list")
    else:
        print("1 is not in the list")

    if 11 not in checkList:
        print("11 is not in the list\n")
    else:
        print("11 is in the list")


def concatString():
    print("This is the first string " + "concatenated with this second string\n")


def stringInterpolation():
    string1 = "string"
    string2 = "second"
    print("This is the first %s and this is the %s string interpolated within the main string." % (string1, string2), '\n')


def fStrings():
    name = "John"
    age = 25
    print(f"My name is {name} and I'm {age} years old.\n")


def stringMethods(string):
    print(f"String: {string}")
    print(f"isalpha(): {string.isalpha()}")
    print(f"isalnum(): {string.isalnum()}")
    print(f"isdecimal(): {string.isdecimal()}")
    print(f"isspace(): {string.isspace()}")
    print(f"istitle(): {string.istitle()}", '\n')


def isNumeric():
    while True:
        num = input("Enter a number between 1 and 10: ")
        if num.isnumeric() and int(num) in range(1, 11):
            break
        print("Invalid input. Please try again.")


def startsWith():
    while True:
        string = input("Enter a string that starts with 'hello': ")
        if string.startswith('hello'):
            break
        print("Invalid input. Please try again.")


def listToString(strList):
    return " ".join(strList)


def stringToList(string):
    return string.split()


def stringMethods1(string):
    print(f"Partitioned string: {string.partition(' ')}")
    print(f"Centered string: {string.center(20, '*')}")
    print(f"Stripped string: {string.strip()}")
    print(f"ASCII value of first character: {ord(string[0])}")
    print(f"Character corresponding to ASCII value 97: {chr(97)}")


def copyPaste(string):
    pyperclip.copy(string)
    print(pyperclip.paste())


def verifyUserId():
    valid_user_ids = ["gdrt-8493", "DBTF-6253", "UyHt-8326", "YYrv-5329", "qzrb-8264"]
    while True:
        user_id = input("Please enter a user ID in the format AAAA-####: ")
        getRequirementNum(14)
        print("Validating User ID Format")
        if re.match(r"^[a-zA-Z]{4}-\d{4}$", user_id):
            getRequirementNum(15)
            getRequirementNum(16)
            print("Validating Correct User ID Provided")
            if user_id in valid_user_ids:
                getRequirementNum(17)
                print("Thank you for entering your user id.")
                break
            else:
                print("Invalid user ID. Please try again or type 'exit' to quit.")
        else:
            print("Invalid user ID format. Please try again or type 'exit' to quit.")


def getPhoneNumber():
    while True:
        phone_number = input("Please enter a phone number in the following format: ###-###-###-#### ")
        getRequirementNum(19)
        print("Validating Phone Number Format")
        if re.match(r"^\d{3}-\d{3}-\d{3}-\d{4}$", phone_number):
            return phone_number
        else:
            print("Invalid phone number. Please try again.")


def checkCallDestination(phone_number):
    country_codes = {
        "Andorra": "376",
        "Bolivia": "591",
        "Djibouti": "253",
        "Georgia": "995",
        "Lithuania": "370"
    }
    parts = phone_number.split("-")
    getRequirementNum(20)
    print("Moving to Country Validation")
    if parts[0] in country_codes.values():
        for country, code in country_codes.items():
            getRequirementNum(21)
            print("Validating Country Code")
            if code == parts[0]:
                getRequirementNum(22)
                print(f"Your call has been placed. Thank you for calling {country}.")
                return
    else:
        print("Invalid phone number. Please try again.")
        getPhoneNumber()


def validateNum():
    num = pyip.inputNum(prompt="Enter a number: ")
    print(f"You entered {num}.", '\n')


def validateString():
    string = pyip.inputStr(prompt="Enter a string: ")
    print(f"You entered {string}.", '\n')


def validateOptions():
    options = ["Option 1", "Option 2", "Option 3"]
    for i in range(len(options)):
        print(options[i])
    choice = pyip.inputChoice(options, prompt="Please Select an option from the above list of options")
    print(f"You selected {choice}.", '\n')


def validateYesNo():
    response = pyip.inputYesNo(prompt="Enter yes or no: ")
    print(f"You entered {response}.", '\n')


def validateDate():
    date = pyip.inputDate(prompt="Enter a date (MM/DD/YYYY): ")
    print(f"You entered {date}.", '\n')


def inputInRange():
    response = pyip.inputNum(prompt="Enter a number from 0-100: ", min=0, max=100)
    print(f"You entered {response}.")


def timedInput():
    response = pyip.inputNum(prompt="Enter a number: ", limit=2, timeout=10, default=0)
    print(f"You entered {response}.")


def allowRegexInput():
    response = pyip.inputNum(prompt='Please enter a 4-digit number: ', allowRegexes=[r'^\d{4}$'])
    print(f"You entered {response}.")


def blockRegexInput():
    response = pyip.inputNum(prompt="Enter a number with more than 1 digit: ", blockRegexes=[r'^[0-9]$'])
    print(f"You entered {response}.")


def experience():
    print("This program was a little bit of a long haul.\n"
          "I especially enjoyed the use of the pyinputplus library.\n"
          "This is a great alternative to creating my own input validation loops\n")


def outro():
    print("Thank you for running Program10 - Julian Cotto")
    input("\nPress Enter to Exit...")
