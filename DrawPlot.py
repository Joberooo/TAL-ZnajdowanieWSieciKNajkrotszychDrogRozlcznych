from matplotlib import pyplot as plt


def drawPlot(dataLine, generateDataTime, dijkstraTime, exactTime, allProgramTime, k):
    plt.plot(dataLine, generateDataTime, 'r--', label='generateDataTime')
    plt.plot(dataLine, dijkstraTime, 'y-.', label='dijkstraTime')
    plt.plot(dataLine, exactTime, 'b:', label='exactTime')
    plt.plot(dataLine, allProgramTime, 'k', label='allProgramTime')
    titleText = "Times from the dimension N for k = " + str(k)
    plt.gca().set(ylabel='Time', xlabel='N', title=titleText)
    plt.legend()
    plt.show()
