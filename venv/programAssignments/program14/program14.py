####################################################################
"""
Developer: Julian Cotto
Date: 12/10/2023
File Name: program14.py
Description: This file contains the main function of program14
"""
####################################################################
from program14Functions import getRequirementNum
from program14Functions import intro
from program14Functions import getProgPurpose
from program14Functions import getMain
from program14Functions import experience
from program14Functions import outro


def main():
    getRequirementNum(1)
    intro()
    getRequirementNum(2)
    getProgPurpose()
    getRequirementNum(3)
    getMain()
    getRequirementNum(4)
    experience()
    outro()

    return 0


if __name__ == "__main__":
    main()
else:
    pass
