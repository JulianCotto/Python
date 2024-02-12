####################################################################
"""
Developer: Julian Cotto
Date: 11/18/2023
File Name: program11Functions.py
Description: This file contains the functions for program11.py
"""
####################################################################
import os
import pyperclip
import shutil
import zipfile


def clearClipboard():
    pyperclip.copy('')


def getRequirementNum(num):
    if num == 1:
        print("Requirement 1\n")
    elif num == 2:
        print("Requirement 2\n")
    elif num == 3:
        print("Requirement 3\n")
    elif num == 4:
        print("\nRequirement 4\n")
    elif num == 5:
        print("\nRequirement 5\n")
    elif num == 6:
        print("\nRequirement 6\n")
    elif num == 7:
        print("Requirement 7\n")
    elif num == 8:
        print("Requirement 8\n")
    elif num == 9:
        print("\nRequirement 9\n")
    elif num == 10:
        print("\nRequirement 10\n")
    elif num == 11:
        print("\nRequirement 11\n")
    elif num == 12:
        print("\nRequirement 12\n")
    elif num == 13:
        print("\nRequirement 13")
    elif num == 14:
        print("Requirement 14\n")
    else:
        print("\nRequirement 15\n")


def intro():
    print("This is Program11 - Julian Cotto")
    print("================================\n")


def getProgPurpose():
    print("This program demonstrates reading, writing, and organizing files.”\n")


def getWorkingDir():
    return os.getcwd()


def createDir():
    dirName = input("Enter a directory name to save files to\n")
    try:
        os.mkdir(dirName)
        print(f"Directory '{dirName}' created.")
        inCreated = True
    except FileExistsError:
        print(f"Directory '{dirName}' already exists.")
        inCreated = False

    return inCreated, dirName


def populateFile(fileName):
    print("Enter your content. When you are done, enter 'EOF' on a new line.")
    with open(fileName, 'w') as file:
        while True:
            line = input()
            if line == 'EOF':
                return
            file.write(line + '\n')


def readFile(filePath):
    print(f"\nReading file '{filePath}'...\n")
    with open(filePath, 'r') as file:
        print(file.read())


def createFile(dirName):
    fileCreated = False
    while not fileCreated:
        fileName = input("Enter a file name\n")
        filePath = os.path.join(dirName, fileName)
        if os.path.exists(filePath):
            print(f"File '{fileName}' already exists in directory '{dirName}'. Please enter a different file name.")
        else:
            populateFile(filePath)
            print(f"File '{fileName}' created in directory '{dirName}'.")
            getRequirementNum(6)
            readFile(filePath)
            fileCreated = True
            return fileName, filePath


def correctedFile(dirName, fileData):
    fileCreated = False
    while not fileCreated:
        fileName = input("Enter a name for the new file\n")
        filePath = os.path.join(dirName, fileName)
        if os.path.exists(filePath):
            print(f"File '{fileName}' already exists in directory '{dirName}'. Please enter a different file name.")
        else:
            with open(filePath, 'w') as file:
                file.write(fileData)
            print(f"New file '{fileName}' created in directory '{dirName}'.")
            fileCreated = True
            return fileName


def alterFile(dirName, fileName):
    filePath = os.path.join(dirName, fileName)
    print(f"Modifying file '{fileName}' in directory '{dirName}'...")
    oldString = input("Enter the substring you want to replace\n")
    newString = input("Enter the new string\n")
    with open(filePath, 'r') as file:
        fileData = file.read()
    while oldString not in fileData:
        print(f"The substring '{oldString}' was not found in the file. Please try again.")
        oldString = input("Enter the substring you want to replace\n")
    fileData = fileData.replace(oldString, newString)
    newFileName = correctedFile(dirName, fileData)
    print(f"File '{fileName}' modified.")
    newFilePath = os.path.join(dirName, newFileName)
    readFile(newFilePath)
    return newFileName, newFilePath


def populateClipboard():
    lines = []  # Initialize an empty list to store the lines

    print("Please type your lines. When you are done, type 'DONE'.")

    line = input()  # Get the first line from the user
    while line != 'DONE':
        lines.append(line)  # Add the line to the list
        line = input()  # Get the next line from the user

    # Combine the lines into one string with line breaks
    lines_str = '\n'.join(lines)

    # Copy the lines to the clipboard
    pyperclip.copy(lines_str)

    print("The lines have been copied to the clipboard.")


def getClipboard():
    # Get the current contents of the clipboard
    clipboard_contents = pyperclip.paste()

    # Display the clipboard contents
    print("The current contents of the clipboard are:")
    print(clipboard_contents)


def readNewFileClip(dirName, fileName):
    # Construct the full file path
    filePath = os.path.join(dirName, fileName)

    # Check if the file exists
    if not os.path.isfile(filePath):
        print(f"The file {filePath} does not exist.")
        return

    # Read and print the file contents
    with open(filePath, 'r') as file:
        print(file.read())


def appendToNewFile(dirName, newFileName, file_lines):
    newFilePath = os.path.join(dirName, newFileName)
    while os.path.exists(newFilePath):
        newFileName = input("File already exists. Please enter a new file name: ")
        newFilePath = os.path.join(dirName, newFileName)
    with open(newFilePath, 'w') as newFile:
        newFile.writelines(file_lines)
    print(f"Appended data to new file '{newFileName}' in directory '{dirName}'.")
    return newFilePath


def appendClipFile(dirName, fileName):
    # Construct the full file path
    filePath = os.path.join(dirName, fileName)

    # Get the current contents of the clipboard
    clipboard_contents = pyperclip.paste()

    # Split the clipboard contents into lines
    clipboard_lines = clipboard_contents.split('\n')

    # Read the file contents
    with open(filePath, 'r') as file:
        file_lines = file.readlines()

    # Append the clipboard lines to the file lines
    for i in range(min(len(file_lines), len(clipboard_lines))):
        file_lines[i] = file_lines[i].strip() + ' ' + clipboard_lines[i] + '\n'  # Add a newline character here

    # Write the new contents back to the file
    with open(filePath, 'w') as file:
        file.writelines(file_lines)

    print(f"Appended clipboard contents to '{fileName}' in directory '{dirName}'.")

    getRequirementNum(12)
    newFileName = input("Enter a new file name to append data: ")
    newFilePath = appendToNewFile(dirName, newFileName, file_lines)

    return newFilePath


def createNewDir():
    newDirName = input("Enter a new directory name: ")
    os.makedirs(newDirName, exist_ok=True)
    print(f"Directory '{newDirName}' created.")
    return newDirName


def copyFilesToNewDir(oldDirName, newDirName):
    for filename in os.listdir(oldDirName):
        oldFilePath = os.path.join(oldDirName, filename)
        newFilePath = os.path.join(newDirName, filename)
        shutil.copy2(oldFilePath, newFilePath)
    print(f"Copied files from '{oldDirName}' to '{newDirName}'.")


def compressFilesInNewDir(dirName):
    for filename in os.listdir(dirName):
        if os.path.isfile(os.path.join(dirName, filename)):
            with zipfile.ZipFile(os.path.join(dirName, f"{filename}.zip"), 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(os.path.join(dirName, filename))
            os.remove(os.path.join(dirName, filename))  # Delete the original file
    print(f"Compressed each file in '{dirName}' into individual .zip files and deleted the original files.")


def experience():
    print("This program helped me understand file manipulation better.\n"
          "I added my own functionality and error protection to it.\n"
          "I am proud of the final product.\n")


def outro():
    print("Thank you for running Program11 - Julian Cotto")
    input("\nPress Enter to Exit...")
