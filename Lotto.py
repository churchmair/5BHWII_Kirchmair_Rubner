import random



if __name__ == '__main__':
    pickedNumber = []
    numLeft = 0
    while numLeft < 6:
        randomNum = random.randint(1, 45)
        if pickedNumber.__contains__(randomNum):
            continue
        else:
            pickedNumber.append(randomNum)
            numLeft += 1
    print("Today's Lotto Numbers are: ")
    print(pickedNumber)


