####################################################################
"""
Developer: Julian Cotto
Date: 11/18/2023
File Name: program11.py
Description: This file contains the main function for program11.py
"""
####################################################################
from program11Functions import clearClipboard
from program11Functions import intro
from program11Functions import getProgPurpose
from program11Functions import getRequirementNum
from program11Functions import getWorkingDir
from program11Functions import createDir
from program11Functions import createFile
from program11Functions import alterFile
from program11Functions import populateClipboard
from program11Functions import getClipboard
from program11Functions import appendClipFile
from program11Functions import readFile
from program11Functions import createNewDir
from program11Functions import copyFilesToNewDir
from program11Functions import compressFilesInNewDir
from program11Functions import experience
from program11Functions import outro


def main():
    dirName = None
    created = False

    getRequirementNum(1)
    intro()

    getRequirementNum(2)
    getProgPurpose()

    getRequirementNum(3)
    print(getWorkingDir())

    getRequirementNum(4)
    while not created:
        created, dirName = createDir()

    getRequirementNum(5)
    fileName, filePath = createFile(dirName)

    getRequirementNum(7)
    fileName, filePath = alterFile(dirName, fileName)

    getRequirementNum(8)
    clearClipboard()
    populateClipboard()

    getRequirementNum(9)
    getClipboard()

    getRequirementNum(10)
    readFile(filePath)
    getClipboard()

    getRequirementNum(11)
    filePath = appendClipFile(dirName, fileName)

    getRequirementNum(13)
    readFile(filePath)

    getRequirementNum(14)
    newDirName = createNewDir()
    copyFilesToNewDir(dirName, newDirName)
    compressFilesInNewDir(newDirName)

    getRequirementNum(15)
    experience()
    outro()

    return


if __name__ == '__main__':
    main()
else:
    pass
