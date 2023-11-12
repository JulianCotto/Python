####################################################################
"""
Developer: Julian Cotto
Date: 11/12/2023
File Name: program010.py
Description: This file contains the main function for program10.py
"""
####################################################################
from program10Functions import getRequirementNum
from program10Functions import intro
from program10Functions import getProgPurpose
from program10Functions import displayEscapeChars
from program10Functions import displayEscapeCharsRaw
from program10Functions import singleTripleQuotes
from program10Functions import doubleTripleQuotes
from program10Functions import indexedCharacters
from program10Functions import inAndNotOps
from program10Functions import concatString
from program10Functions import stringInterpolation
from program10Functions import fStrings
from program10Functions import stringMethods
from program10Functions import isNumeric
from program10Functions import startsWith
from program10Functions import listToString
from program10Functions import stringToList
from program10Functions import stringMethods1
from program10Functions import copyPaste
from program10Functions import verifyUserId
from program10Functions import getPhoneNumber
from program10Functions import checkCallDestination
from program10Functions import validateNum
from program10Functions import validateString
from program10Functions import validateOptions
from program10Functions import validateYesNo
from program10Functions import validateDate
from program10Functions import inputInRange
from program10Functions import timedInput
from program10Functions import allowRegexInput
from program10Functions import blockRegexInput
from program10Functions import experience
from program10Functions import outro


def main() -> None:
    getRequirementNum(1)
    intro()

    getRequirementNum(2)
    getProgPurpose()

    getRequirementNum(3)
    displayEscapeChars()
    displayEscapeCharsRaw()
    singleTripleQuotes()
    doubleTripleQuotes()

    getRequirementNum(4)
    singleIndexed, fifthFromLast, threeUntilEnd, upTillSeventh = indexedCharacters()
    print("Single Indexed Character:", singleIndexed)
    print("Character 5 Index Places From the End:", fifthFromLast)
    print("Characters from 3 until Last:", threeUntilEnd)
    print("Characters from Beginning Until 7 (non-inclusive):", upTillSeventh, '\n')

    getRequirementNum(5)
    inAndNotOps()

    getRequirementNum(6)
    concatString()
    stringInterpolation()
    fStrings()

    getRequirementNum(7)
    stringMethods("HelloWorld")
    stringMethods("HelloWorld123")
    stringMethods("123")
    stringMethods(" ")
    stringMethods("Hello World")

    getRequirementNum(8)
    isNumeric()
    startsWith()

    getRequirementNum(9)
    strList = ["This", "is", "a", "list", "of", "strings"]
    print(listToString(strList), '\n')

    getRequirementNum(10)
    string = "This string will be converted to a list of strings"
    print(stringToList(string), '\n')

    getRequirementNum(11)
    string = "Hello, World!"
    stringMethods1(string)

    getRequirementNum(12)
    stringToPyper = "Hello, World!"
    copyPaste(stringToPyper)

    getRequirementNum(13)
    verifyUserId()

    getRequirementNum(18)
    phone_number = getPhoneNumber()
    checkCallDestination(phone_number)

    getRequirementNum(23)
    validateNum()
    validateString()
    validateOptions()
    validateYesNo()
    validateDate()

    getRequirementNum(24)
    inputInRange()
    timedInput()
    allowRegexInput()
    blockRegexInput()

    getRequirementNum(25)
    experience()
    outro()

if __name__ == '__main__':
    main()
else:
    pass
