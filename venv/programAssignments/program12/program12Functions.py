####################################################################
"""
Developer: Julian Cotto
Date: 11/24/2023
File Name: program12Functions.py
Description: This file contains the functions for program12.py
"""
####################################################################
import pyperclip
import webbrowser
import requests
import openpyxl
import random
import string
import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class ExcelProcessing:
    def __init__(self, filename):
        if os.path.exists(filename):
            self.wb = openpyxl.load_workbook(filename)
        else:
            self.wb = openpyxl.Workbook()
            self.wb.save(filename)

    def getSheets(self):
        return self.wb.sheetnames

    def getAndSelectCells(self, sheet_name):
        while sheet_name not in self.wb.sheetnames:
            print(f"No sheet named '{sheet_name}' found in the workbook.")
            sheet_name = input("Please enter a valid sheet name:\n")
        sheet = self.wb[sheet_name]
        getRequirementNum(7)
        print(f"The sheet has data up to cell {sheet.dimensions}")
        while True:
            cell = input("Enter a cell (e.g. B7)\n")
            try:
                print(sheet[cell].value)
                break
            except KeyError:
                print("Invalid cell. Please enter a valid cell.")

    def returnAreaData(self, sheet_name):
        if sheet_name in self.wb.sheetnames:
            sheet = self.wb[sheet_name]
            while True:
                area = input("Enter a rectangular section (e.g. A3:C7)\n")
                try:
                    cells = sheet[area]
                    for row in cells:
                        print(' '.join(str(cell.value) for cell in row))
                    break
                except KeyError:
                    print("Invalid area. Please enter a valid rectangular section.")
        else:
            print(f"No sheet named '{sheet_name}' found in the workbook.")

    def createAndPopulateWorkbook(self):
        self.wb = openpyxl.Workbook()
        self.wb.remove(self.wb.active)
        num_sheets = random.randint(1, 5)
        for i in range(num_sheets):
            sheet = self.wb.create_sheet(title=f'Sheet{i + 1}')
            for row in sheet.iter_rows(min_row=1, max_row=10, min_col=1, max_col=5):
                for cell in row:
                    cell.value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        self.wb.save('example.xlsx')

    def getSheetName(self):
        sheetName = input("Please enter the name of the sheet to query\n")
        return sheetName


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
        print("\nRequirement 7\n")
    elif num == 8:
        print("\nRequirement 8\n")
    else:
        print("\nRequirement 9\n")


def intro():
    print("This is Program12 - Julian Cotto")
    print("================================\n")


def getProgPurpose():
    print("This program demonstrates using Python to perform web scraping and working with Excel spreadsheets.\n")


def getAddress():
    address = input("Enter a street address to search\n")
    pyperclip.copy(address)


def fetchAddress():
    address = pyperclip.paste()
    webbrowser.open('https://www.google.com/maps/place/' + address)


def scrapePage():
    while True:
        url = input("Enter the full URL of a web page including http\n")
        if valid_url(url):
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                paragraphs = soup.find_all('p')
                if paragraphs:
                    for p in paragraphs:
                        print(p.get_text())
                    break
                else:
                    print("No <p></p> elements detected on the page")
            except requests.exceptions.RequestException as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid URL. Please enter a valid URL.")


def getExcelFileName():
    fileName = input("Enter excel file name to open or create\n")
    return fileName


def valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def experience():
    print("This was a fun program that I can apply at work.\n"
          "I regularly wok with databases and excel files.\n"
          "I will be able to easily automate some of the steps.\n")


def outro():
    print("Thank you for running Program12 - Julian Cotto")
    input("\nPress Enter to Exit...")

