####################################################################
# Developer: Julian Cotto
# Date: 9/10/2023
# File Name: program03Functions.py
# Description: This file contains the functions for program03.py
####################################################################

def intro():
    print("This is Program 3 - Julian Cotto")
    print("================================\n")

    print("Requirement 2\n")
    print("This program records goals for soccer players and points for basketball players.\n")

def getPlayers(sport):
    players = []
    for i in range(0, 3):
        player = input("Enter the name of a " + sport + " player #" + str(i+1) + ":\n")
        players.append(player)
    return players

def getGoals(players):
    goals = []
    for i in range(len(players)):
        goals.append(int(input("Enter the number of goals for " + players[i] + ":\n")))
    return goals

def sortData(players, goals):
    for i in range(len(goals)):
        for j in range(i+1, len(goals)):
            if goals[i] < goals[j]:
                temp = goals[i]
                goals[i] = goals[j]
                goals[j] = temp
                temp = players[i]
                players[i] = players[j]
                players[j] = temp
    return players, goals

def compileData(sport, sortedPlayers, sortedGoals):
    print(sport, "Players in sorted order:")
    for i in range(len(sortedPlayers)):
        print(sortedPlayers[i] + ":", sortedGoals[i])

def experience():
    print("Program03 was a quick exercise.\n"
          "I compare it to a light jog.\n"
          "I'm looking forward to the more complex work to come.\n")

def outro():
    print("Thank you for running Program 3 - Julian Cotto")
    input("\nPress Enter to Exit...")