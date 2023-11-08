import random




def statisticsPoker(nrPlays):
    cardsPerHand = 5
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
        else:statisticDrawnHands[0] += 1

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


def checkHand(pickedHand):
    checkHands = []
    for i in range(0, 13):
        checkHands.append(0)
    for j in pickedHand:
        checkHands[j[1]] += 1
    return checkHands


def checkOnePair(pickedHand):
    currentHand = checkHand(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 2) and (currentHand[1] != 2)):
        return True


def checkTwoPair(pickedHand):
    currentHand = checkHand(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 2) and (currentHand[1] == 2)):
        return True


def checkThreeOfAKind(pickedHand):
    currentHand = checkHand(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 3) and (currentHand[1] != 2)):
        return True


def checkFourIfAKind(pickedHand):
    currentHand = checkHand(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if (currentHand[0] == 4):
        return True


def checkFullHouse(pickedHand):
    currentHand = checkHand(pickedHand)
    currentHand.sort(key=None, reverse=True)
    if ((currentHand[0] == 3) and currentHand[1] == 2):
        return True


def checkStraight(pickedHand):
    currentHand = checkHand(pickedHand)
    for a in range(0, 9):
        if ((currentHand[a] == 1) and (currentHand[a + 1] == 1) and (currentHand[a + 2] == 1) and (currentHand[a + 3] == 1) and (currentHand[a + 4] == 1)):
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
    currentHand = checkHand(pickedHand)


    for f in range(0, 4):
        checkHandsFlush.append(0)

    for j in pickedHand:
        checkHandsFlush[j[0]] += 1
    checkHandsFlush.sort(key=None, reverse=True)

    if (checkHandsFlush[0] == 5):
        isFlush = True

    for a in range(0, 9):
        if ((currentHand[a] == 1) and (currentHand[a + 1] == 1) and (currentHand[a + 2] == 1) and (currentHand[a + 3] == 1) and (currentHand[a + 4] == 1)):
            isStraight = True

    if isStraight and isFlush:
        return True


def checkRoyalFlush(pickedHand):
    currentHand = checkHand(pickedHand)
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


if __name__ == '__main__':

    statisticsPoker(1000000)
    #print(statisticDrawnHands)






