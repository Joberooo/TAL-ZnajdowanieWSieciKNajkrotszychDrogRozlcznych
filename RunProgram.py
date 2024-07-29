from typing import List
from CompleteProgram import completeAlgorithm
from DrawPlot import drawPlot


def runSingleProgram(data: List, k: int) -> None:
    outcome = []
    for i in data:
        outcome.append(completeAlgorithm(*i))

    dataLine = []
    generateDataTime = []
    dijkstraTime = []
    exactTime = []
    allProgramTime = []
    for i, result in enumerate(outcome):
        dataLine.append(data[i][0])
        generateDataTime.append(result[0])
        dijkstraTime.append(result[1])
        exactTime.append(result[4])
        allProgramTime.append(result[6])

        for j, path in enumerate(result[2]):
            print(f"Path nr: {j+1}/{data[i][1]}")
            print(path)
            print(f"Path weight is: {result[3][j]}")

        for j, path in enumerate(result[5]):
            print(f"Path nr: {j+1}/{data[i][1]}")
            print(path[0])
            print(f"Path weight is: {path[1]}")

    drawPlot(dataLine, generateDataTime, dijkstraTime, exactTime, allProgramTime, k)
