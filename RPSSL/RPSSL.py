import os
import random
import requests
from dotenv import load_dotenv
load_dotenv()

def movePlayer():
    correctMove = False
    while(correctMove == False):
        print("possible moves: rock, paper, scisoors, spock, lizard")
        pickPlayer = input("make a move: ")
        for dictPicks in possiblePicks.values():
            if(pickPlayer == dictPicks):
                stats[pickPlayer] += 1
                return pickPlayer


def moveComputer():
    pickComputer = random.randrange(5)
    return possiblePicks[pickComputer]


def checkWinner(moveP, moveC):
    if((moveP == "rock" and moveC == " ") or (moveP == "rock" and moveC == "scissors")):
        return True

    elif((moveP == "paper" and moveC == "rock") or (moveP == "paper" and moveC == "spock")):
        return True

    elif((moveP == "scissors" and moveC == "paper") or (moveP == "scissors" and moveC == "lizard")):
        return True

    elif((moveP == "spock" and moveC == "rock") or (moveP == "spock" and moveC == "scissors")):
        return True

    elif((moveP == "lizard" and moveC == "spock") or (moveP == "lizard" and moveC == "paper")):
        return True
    elif(moveP == moveC):
        return None
    else:
        return False


def statistics(winner):
    if (winner):
        stats["player"] += 1
    elif (winner == False):
        stats["computer"] += 1
    else:
        stats["draw"] += 1
    return stats


# statsWins = {"player": 0, "computer": 0, "draw": 0}
# statsPicks = {"rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}


def game():
    anotherRound = True

    while True:
        print("Menu: ")
        print("play ... p")
        print("stats ... s")
        print("save stats ... a")
        choice = input("Choose action: ")
        if (choice == "p"):
            while (anotherRound):
                moveP = movePlayer()
                moveC = moveComputer()
                print("Computer picked: " + str(moveC))

                winner = checkWinner(moveP, moveC)
                statistics(winner)

                choice = input(print("Do you want to play again? [y, n]"))
                if (choice == "n"):
                    anotherRound = False
                else:
                    anotherRound = True
        elif (choice == "s"):
            print("#################")
            print("Statistic:")
            print(stats)
            print("#################")

        elif (choice == "a"):
            requests.post(os.getenv("SERVER_URL") + "/saveStats", json=stats)
            print("stats saved")


if __name__ == "__main__":
    keys = ["player", "computer", "draw", "rock", "paper", "scissors", "spock", "lizard"]

    stats = requests.get(os.getenv("SERVER_URL") + "/getStats").json()
    stats = {k: v for (k, v) in zip(keys, stats)}

    print("aktuelle Stats: " + str(stats))
    possiblePicks = {0: "rock", 1: "paper", 2: "scissors", 3: "spock", 4: "lizard"}

    game()
