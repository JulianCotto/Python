####################################################################
"""
Developer: Julian Cotto
Date: 12/3/2023
File Name: program13Functions.py
Description: This file contains the functions for program13.py
"""
####################################################################
import os
import csv
import json
from PyPDF2 import PdfReader
from docx import Document


class PDFProcessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_number_of_pages(self):
        pdf = PdfReader(self.file_path)
        return len(pdf.pages)

    def get_page_content(self, page_number):
        pdf = PdfReader(self.file_path)
        page = pdf.pages[page_number - 1]
        return page.extract_text()


class WordProcessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_number_of_paragraphs(self):
        doc = Document(self.file_path)
        return len(doc.paragraphs)

    def get_paragraph(self, paragraph_number):
        doc = Document(self.file_path)
        return doc.paragraphs[paragraph_number - 1].text


class CSVProcessing:
    def __init__(self, file_path):
        self.file_path = file_path

    def display_contents(self):
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
            for row in data:
                print(row)
            print(f"Data range: {len(data)} rows x {len(data[0]) if data else 0} columns")

    def enter_data(self):
        data = input("Enter new data (comma-separated): ")
        if ',' in data:
            data = data.split(',')
        else:
            data = [data]
        self.update_csv(data)

    def update_csv(self, data):
        with open(self.file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, lineterminator=os.linesep)
            writer.writerow(data)

    def update_data(self):
        row = int(input("Enter the row number of the cell to update: ")) - 1
        col = int(input("Enter the column number of the cell to update: ")) - 1
        new_data = input("Enter the new data for the cell: ")
        with open(self.file_path, 'r') as file:
            data = list(csv.reader(file))
        data[row][col] = new_data
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)


class JSONProcessing:
    def __init__(self):
        self.data = {}

    def add_city(self, city, adjective):
        self.data[city] = adjective

    def display_json(self):
        return json.dumps(self.data)


def getRequirementNum(num):
    if num == 1:
        print("\nRequirement 1\n")
    elif num == 2:
        print("\nRequirement 2\n")
    elif num == 3:
        print("\nRequirement 3\n")
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
    elif num == 9:
        print("\nRequirement 9\n")
    elif num == 10:
        print("\nRequirement 10\n")
    elif num == 11:
        print("\nRequirement 11\n")
    elif num == 12:
        print("\nRequirement 12\n")


def intro():
    print("This is Program13 - Julian Cotto")
    print("================================")


def getProgPurpose():
    print("This program demonstrates using Python to work with PDF and MS Word documents, and CSV and JSON data.")


def experience():
    print("Classes have always been a little.\n"
          "bit for me to understand and work with.\n"
          "I'm happy to be getting so much practice'.\n")


def outro():
    print("Thank you for running Program13 - Julian Cotto")
    input("\nPress Enter to Exit...")
