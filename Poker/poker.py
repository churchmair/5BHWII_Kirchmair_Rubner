import functools
import random
import sys
import time


def statisticsPoker(nrPlays, cardsPerHand):
    statisticDrawnHands = []

    for i in range(0, 10):
        statisticDrawnHands.append(0)

    for i in range(nrPlays):
        currentHand = getHand(cardsPerHand)

        if checkRoyalFlush(currentHand):
            statisticDrawnHands[9] += 1
        elif checkStraightFlush(currentHand):
            statisticDrawnHands[8] += 1
        elif checkFourIfAKind(currentHand):
            statisticDrawnHands[7] += 1
        elif checkFullHouse(currentHand):
            statisticDrawnHands[6] += 1
        elif checkFlush(currentHand):
            statisticDrawnHands[5] += 1
        elif checkStraight(currentHand):
            statisticDrawnHands[4] += 1
        elif checkThreeOfAKind(currentHand):
            statisticDrawnHands[3] += 1
        elif checkTwoPair(currentHand):
            statisticDrawnHands[2] += 1
        elif checkOnePair(currentHand):
            statisticDrawnHands[1] += 1
        else:
            statisticDrawnHands[0] += 1

    print("Probability of Highcards: " + str(statisticDrawnHands[0] / nrPlays * 100) + "%")
    print("Probability of One Pair: " + str(statisticDrawnHands[1] / nrPlays * 100) + "%")
    print("Probability of Two Pair: " + str(statisticDrawnHands[2] / nrPlays * 100) + "%")
    print("Probability of Three Of A Kind: " + str(statisticDrawnHands[3] / nrPlays * 100) + "%")
    print("Probability of Straight: " + str(statisticDrawnHands[4] / nrPlays * 100) + "%")
    print("Probability of Flush: " + str(statisticDrawnHands[5] / nrPlays * 100) + "%")
    print("Probability of Full House: " + str(statisticDrawnHands[6] / nrPlays * 100) + "%")
    print("Probability of Four Of A Kind: " + str(statisticDrawnHands[7] / nrPlays * 100) + "%")
    print("Probability of Straight Flush: " + str(statisticDrawnHands[8] / nrPlays * 100) + "%")
    print("Probability of Royal Flush: " + str(statisticDrawnHands[9] / nrPlays * 100) + "%")

    print(statisticDrawnHands)


def getHand(nrCards):
    currentHand52 = []
    currentHand_tuple = []

    pickedCards = 0
    while pickedCards < nrCards:
        randomCard = random.randint(1, 52)
        if currentHand52.__contains__(randomCard):
            continue
        else:
            currentHand52.append(randomCard)
            color = currentHand52[pickedCards] // 14
            number = currentHand52[pickedCards] % 13
            pickedCards += 1
            currentHand_tuple.append((color, number))

    return currentHand_tuple


def countCards(pickedHand):
    checkHands = []
    for i in range(0, 13):
        checkHands.append(0)
    for j in pickedHand:
        checkHands[j[1]] += 1
    return checkHands
    # returns [0, 0, 0, 0 ,0, 1, 1, 0, 1, 1, 1, 0, 0 ]


def checkOnePair(pickedHand):
    currentHand = countCards(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 2) and (currentHand[1] != 2)):
        return True


def checkTwoPair(pickedHand):
    currentHand = countCards(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 2) and (currentHand[1] == 2)):
        return True


def checkThreeOfAKind(pickedHand):
    currentHand = countCards(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 3) and (currentHand[1] != 2)):
        return True


def checkFourIfAKind(pickedHand):
    currentHand = countCards(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if (currentHand[0] == 4):
        return True


def checkFullHouse(pickedHand):
    currentHand = countCards(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 3) and currentHand[1] == 2):
        return True


def checkStraight(pickedHand):
    currentHand = countCards(pickedHand)
    for a in range(0, 10):
        if ((currentHand[a] == 1) and (currentHand[a + 1] == 1) and (currentHand[a + 2] == 1) and (
                currentHand[a + 3] == 1) and (currentHand[(a + 4) % 13] == 1)):
            return True


def checkFlush(pickedHand):
    checkHandsFlush = []
    for f in range(0, 4):
        checkHandsFlush.append(0)

    for j in pickedHand:
        checkHandsFlush[j[0]] += 1
    checkHandsFlush.sort(key=None, reverse=True)

    if (checkHandsFlush[0] == 5):
        return True


def checkStraightFlush(pickedHand):
    isFlush, isStraight = False, False
    checkHandsFlush = []
    currentHand = countCards(pickedHand)

    for f in range(0, 4):
        checkHandsFlush.append(0)

    for j in pickedHand:
        checkHandsFlush[j[0]] += 1
    checkHandsFlush.sort(key=None, reverse=True)

    if (checkHandsFlush[0] == 5):
        isFlush = True

    for a in range(0, 9):
        if ((currentHand[a] == 1) and (currentHand[a + 1] == 1) and (currentHand[a + 2] == 1) and (
                currentHand[a + 3] == 1) and (currentHand[a + 4] == 1)):
            isStraight = True

    if isStraight and isFlush:
        return True


def checkRoyalFlush(pickedHand):
    currentHand = countCards(pickedHand)
    checkHandsFlush = []
    isFlush = False
    for f in range(0, 4):
        checkHandsFlush.append(0)

    for j in pickedHand:
        checkHandsFlush[j[0]] += 1
    checkHandsFlush.sort(key=None, reverse=True)

    if (checkHandsFlush[0] == 5):
        isFlush = True

    if ((currentHand[8] == 1) and (currentHand[9] == 1) and (currentHand[10] == 1) and (
            currentHand[11] == 1) and (currentHand[12] == 1) and isFlush):
        return True

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        #with open("test.txt", "a") as file:
        #    file.write(func.__name__)
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def runGames(nrPlays, cardsPerHand):
    statisticsPoker(nrPlays, cardsPerHand)

def main():
    nrPlays = int(sys.argv[1])
    cardsPerHand = int(sys.argv[2])

    #so würds normalerweise gehen
    #statisticsPoker(nrPlays, cardsPerHand)

    runGames(nrPlays, cardsPerHand)


if __name__ == '__main__':
    main()
