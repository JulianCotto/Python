####################################################################
# Developer: Julian Cotto
# Date: 9/10/2023
# File Name: program03.py
# Description: This file contains the functions for program03.py
####################################################################
from program03Functions import intro
from program03Functions import getPlayers
from program03Functions import getGoals
from program03Functions import sortData
from program03Functions import compileData
from program03Functions import experience
from program03Functions import outro
def main() -> None:
    sport = "Soccer"

    print("Requirement 1\n")
    intro()
    print("Requirement 3\n")
    players = getPlayers(sport)
    print("\nRequirement 4\n")
    goals = getGoals(players)
    print("\nRequirement 5 - (Sorting Data in Background)\n")
    sortedPlayers, sortedGoals = sortData(players, goals)
    print("\nRequirement 6\n")
    compileData(sport, players, goals)

    sport = "Basketball"

    print("\nRequirement 7\n")
    players = getPlayers(sport)
    print("\nRequirement 8\n")
    goals = getGoals(players)
    print("\nRequirement 9 - (Sorting Data in Background)\n")
    sortedPlayers, sortedGoals = sortData(players, goals)
    print("\nRequirement 10\n")
    compileData(sport, players, goals)
    print("\nRequirement 11\n")
    experience()
    outro()


if __name__ == '__main__':
        main()