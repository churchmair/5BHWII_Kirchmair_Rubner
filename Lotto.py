import random
from matplotlib import pyplot as plt

pickedNumber = []
dict_statistic = {}
for i in range(46):
    dict_statistic[i] = 0

def lotto():

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

def statistic(numberRuns):
    for i in range(numberRuns):
        randNumber = random.randint(0, 45)
        dict_statistic[randNumber] = dict_statistic[randNumber] + 1
    return dict_statistic



if __name__ == '__main__':
    lotto()

    print("Stats after 1000 runs")
    print(statistic(100))

    xAxis = list(dict_statistic.keys())
    yAxis = list(dict_statistic.values())
    plt.bar(range(len(dict_statistic)), yAxis, tick_label=xAxis)
    plt.show()



