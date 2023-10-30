####################################################################
# Developer: Julian Cotto
# Date: 10/27/2023
# File Name: program08.py
# Description: This file contains the main function for program08.py
####################################################################
from program08Functions import intro
from program08Functions import getProgPurpose
from program08Functions import getRequirementNum
from program08Functions import addPokedexEntry
from program08Functions import getPokedexEntries
from program08Functions import experience
from program08Functions import outro


def main() -> None:
    getRequirementNum(1)
    intro()
    getRequirementNum(2)
    getProgPurpose()
    getRequirementNum(3)
    pokedex = addPokedexEntry()
    getRequirementNum(4)
    getPokedexEntries(pokedex)
    getRequirementNum(5)
    experience()
    outro()


if __name__ == '__main__':
    main()
else:
    pass