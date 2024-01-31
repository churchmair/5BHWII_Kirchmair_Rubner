import random


def movePlayer():
    correctMove = False
    while(correctMove == False):
        print("possible moves: rock, paper, scisoors, spock, lizard")
        pickPlayer = input("make a move: ")
        for dictPicks in possiblePicks.values():
            if(pickPlayer == dictPicks):
                statsPicks[pickPlayer] +=1
                return pickPlayer


def moveComputer():
    pickComputer = random.randrange(5)
    statsPicks[possiblePicks[pickComputer]] += 1
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


def stats(winner):
    if (winner):
        statsWins["player"] += 1
    elif (winner == False):
        statsWins["computer"] += 1
    else:
        statsWins["draw"] += 1
    return statsWins


if __name__ == "__main__":
    statsWins = {"player": 0, "computer": 0, "draw": 0}
    statsPicks = {"rock": 0, "paper": 0, "scissors": 0, "spock": 0, "lizard": 0}
    possiblePicks = {0: "rock", 1: "paper", 2: "scissors", 3: "spock", 4: "lizard"}
    anotherRound = True

    while True:
        print("Menu: ")
        print("play ... p")
        print("stats ... s")
        choice = input("Choose action: ")
        if(choice == "p"):
            while(anotherRound):
                moveP = movePlayer()
                moveC = moveComputer()
                print("Computer picked: " + str(moveC))

                winner = checkWinner(moveP, moveC)
                stats(winner)

                choice = input(print("Do you want to play again? [y, n]"))
                if(choice == "n"):
                    anotherRound = False
                else:
                    anotherRound = True
        elif(choice == "s"):
            print("#################")
            print("Statistic: Wins")
            print(statsWins)
            print("Statistic: Picks")
            print(statsPicks)
            print("#################")
