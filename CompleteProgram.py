import copy
import time

from DrawGraph import generateGraph
from FindPath import calcPathWeight, findAllShortestPathsDijkstra, findAllSimplePaths, changeToEdgesTable, \
    findDisjointRoads
from GraphGenerator import generateGraphData


def completeAlgorithm(n, k, a, b, minWeight, maxWeight, timeLimit, roundLimit):
    globalStart = time.time()
    generateStart = time.time()
    N = n
    k = k
    A = a
    B = b
    if A == B:
        print("wrong data entered, correct and run the code again!")
        return
    minWeight = minWeight
    maxWeight = maxWeight
    timeLimit = timeLimit

    data = generateGraphData(N, minWeight, maxWeight, roundLimit)
    graph = generateGraph(data, roundLimit)

    start = time.time()
    print("Start copping graph...")
    graphCopy = copy.deepcopy(graph)
    print("Graph copied in: " + str(round(time.time() - start, roundLimit)) + "\n")
    generateDataTime = round(time.time() - generateStart, roundLimit)
    print("----- Generate data and graph finished in: " + str(generateDataTime) + "\n")

    print("------------------------------- DIJKSTRA -------------------------------")
    dijkstraStart = time.time()
    allShortestPaths = findAllShortestPathsDijkstra(graphCopy, A, B, k, roundLimit)
    allShortestPathsWeights = []
    summaryWeight = 0
    for i in range(len(allShortestPaths)):
        print("Path nr: " + str(i + 1) + "/" + str(k))
        print(allShortestPaths[i])
        value = calcPathWeight(data[1], allShortestPaths[i])
        allShortestPathsWeights.append(value)
        summaryWeight += value
    print("Summary all shortest paths weight is (Dijkstra): " + str(round(summaryWeight, 2)) + "\n")
    dijkstraAlgorithmTime = round(time.time() - dijkstraStart, roundLimit)
    print("----- Dijkstra finished in: " + str(dijkstraAlgorithmTime) + "\n")

    print("--------------------------- EXACT ALGORITHM ----------------------------")
    exactStart = time.time()
    allPaths = findAllSimplePaths(graph, A, B, data[1], roundLimit)
    print("Number of roads found: " + str(len(allPaths)))
    allPaths, startEdges, stopEdges = changeToEdgesTable(allPaths, data[1], data[2], A, B)
    disjointRoads = findDisjointRoads(allPaths, k, timeLimit, roundLimit, startEdges, stopEdges)
    for i in range(len(disjointRoads)):
        print("Path nr: " + str(i + 1) + "/" + str(k))
        print(disjointRoads[i][0])
        print("Path weight is: " + str(disjointRoads[i][1]) + "\n")
    exactAlgorithmTIme = round(time.time() - exactStart, roundLimit)
    print("----- Exact algorithm finished in: " + str(exactAlgorithmTIme) + "\n")

    allProgramTime = round(time.time() - globalStart, roundLimit)
    print("Program finished in: " + str(allProgramTime) + "\n")

    print("--------------------------- Final Data ----------------------------")
    print("generateDataTime: " + str(generateDataTime))
    print("dijkstraAlgorithmTime: " + str(dijkstraAlgorithmTime))
    print("exactAlgorithmTIme: " + str(exactAlgorithmTIme))
    print("allProgramTime: " + str(allProgramTime))

    return [generateDataTime,
            dijkstraAlgorithmTime, allShortestPaths, allShortestPathsWeights,
            exactAlgorithmTIme, disjointRoads,
            allProgramTime]
