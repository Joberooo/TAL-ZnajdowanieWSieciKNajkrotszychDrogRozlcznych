from CompleteProgram import completeAlgorithm
from DrawPlot import drawPlot


def runSingleProgram(data, k):
    outcome = []
    for i in data:
        print("\n--------------------------- START COMPLETE ALGORITHM FOR NEW DATA ----------------------------")
        print(i)
        print("----------------------------------------------------------------------------------------------")
        outcome.append(completeAlgorithm(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        print("-------------------------------------------------------------------")

    dataLine = []
    generateDataTime = []
    dijkstraTime = []
    exactTime = []
    allProgramTime = []
    for i in range(len(outcome)):
        print("--------------------------- OUTCOME[" + str(i) + "] ----------------------------")
        dataLine.append(data[i][0])
        print("generateDataTime: " + str(outcome[i][0]))
        generateDataTime.append(outcome[i][0])
        print("dijkstraAlgorithmTime: " + str(outcome[i][1]))
        dijkstraTime.append(outcome[i][1])
        print("exactAlgorithmTIme: " + str(outcome[i][4]))
        exactTime.append(outcome[i][4])
        print("allProgramTime: " + str(outcome[i][6]))
        allProgramTime.append(outcome[i][6])
        print("-------------------------------------------------------------------")
        for j in range(len(outcome[i][2])):
            print("Path nr: " + str(j + 1) + "/" + str(data[i][1]))
            print(outcome[i][2][j])
            print("Path weight is: " + str(outcome[i][3][j]))
        print("-------------------------------------------------------------------")
        for j in range(len(outcome[i][5])):
            print("Path nr: " + str(j + 1) + "/" + str(data[i][1]))
            print(outcome[i][5][j][0])
            print("Path weight is: " + str(outcome[i][5][j][1]))
        print("-------------------------------------------------------------------")

    drawPlot(dataLine, generateDataTime, dijkstraTime, exactTime, allProgramTime, k)
