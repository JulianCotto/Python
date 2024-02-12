####################################################################
"""
Developer: Julian Cotto
Date: 12/3/2023
File Name: program13.py
Description: This file contains the main function of program13
"""
####################################################################
from program13Functions import PDFProcessing
from program13Functions import WordProcessing
from program13Functions import CSVProcessing
from program13Functions import JSONProcessing
from program13Functions import getRequirementNum
from program13Functions import intro
from program13Functions import getProgPurpose
from program13Functions import experience
from program13Functions import outro


def main():
    getRequirementNum(1)
    intro()
    getRequirementNum(2)
    getProgPurpose()
    getRequirementNum(3)
    pdf = PDFProcessing("meetingminutes.pdf")
    word = WordProcessing("demo.docx")
    csv = CSVProcessing("example.csv")
    json = JSONProcessing()
    print("Objects Initialized")
    getRequirementNum(4)
    print("Number of Pages:", pdf.get_number_of_pages())
    print("\nPage Content",
          getRequirementNum(5),
          pdf.get_page_content(
              int(input("Enter Page to view Content\n"))))
    getRequirementNum(6)
    print("Number of Paragraphs:", word.get_number_of_paragraphs())
    print("\nParagraph Content",
          getRequirementNum(7),
          word.get_paragraph(
              int(input("Enter Paragraph Number to view Content\n"))))
    getRequirementNum(8)
    csv.display_contents()
    getRequirementNum(9)
    csv.enter_data()
    csv.update_data()
    getRequirementNum(10)
    for i in range(0, 6):
        json.add_city(input("Enter City\n"), input("Enter Description\n"))
    getRequirementNum(11)
    print(json.display_json())
    getRequirementNum(12)
    experience()
    outro()

    return


if __name__ == "__main__":
    main()
else:
    pass
