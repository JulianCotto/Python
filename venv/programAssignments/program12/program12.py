####################################################################
"""
Developer: Julian Cotto
Date: 11/24/2023
File Name: program12.py
Description: This file contains the main function of program12
"""
####################################################################
from program12Functions import ExcelProcessing
from program12Functions import getRequirementNum
from program12Functions import intro
from program12Functions import getProgPurpose
from program12Functions import getAddress
from program12Functions import fetchAddress
from program12Functions import scrapePage
from program12Functions import getExcelFileName
from program12Functions import experience
from program12Functions import outro


def main():
    getRequirementNum(1)
    intro()
    getRequirementNum(2)
    getProgPurpose()
    getRequirementNum(3)
    getAddress()
    fetchAddress()
    getRequirementNum(4)
    scrapePage()
    getRequirementNum(5)
    excel = ExcelProcessing(getExcelFileName())
    excel.createAndPopulateWorkbook()
    getRequirementNum(6)
    print(excel.getSheets())
    sheetName = excel.getSheetName()
    excel.getAndSelectCells(sheetName)
    getRequirementNum(8)
    excel.returnAreaData(sheetName)
    getRequirementNum(9)
    experience()
    outro()

    return


if __name__ == "__main__":
    main()
else:
    pass
