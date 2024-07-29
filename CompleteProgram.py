import time
from DrawGraph import generateGraph
from FindPath import (
    calcPathWeight,
    findAllShortestPathsDijkstra,
    findAllSimplePaths,
    changeToEdgesTable,
    findDisjointRoads,
)
from GraphGenerator import generateGraphData


def completeAlgorithm(n, k, a, b, minWeight, maxWeight, timeLimit, roundLimit):
    globalStart = time.time()

    if a == b:
        print("wrong data entered, correct and run the code again!")
        return

    data = generateGraphData(n, minWeight, maxWeight, roundLimit)
    graph = generateGraph(data, roundLimit)

    start = time.time()
    print("Start copying graph...")
    graphCopy = graph.copy()
    print(f"Graph copied in: {str(round(time.time() - start, roundLimit))}\n")
    generateDataTime = round(time.time() - globalStart, roundLimit)
    print(f"----- Generate data and graph finished in: {str(generateDataTime)}\n")

    print("------------------------------- DIJKSTRA -------------------------------")
    dijkstraStart = time.time()
    allShortestPaths = findAllShortestPathsDijkstra(graphCopy, a, b, k, roundLimit)
    allShortestPathsWeights = []
    summaryWeight = 0
    for i, path in enumerate(allShortestPaths):
        print(f"Path nr: {str(i + 1)}/{str(k)}\n{path}")
        value = calcPathWeight(data[1], path)
        allShortestPathsWeights.append(value)
        summaryWeight += value
    print(
        f"Summary all shortest paths weight is (Dijkstra): {str(round(summaryWeight, 2))}\n"
    )
    dijkstraAlgorithmTime = round(time.time() - dijkstraStart, roundLimit)
    print(f"----- Dijkstra finished in: {str(dijkstraAlgorithmTime)}\n")

    print("--------------------------- EXACT ALGORITHM ----------------------------")
    exactStart = time.time()
    allPaths = findAllSimplePaths(graph, a, b, data[1], roundLimit)
    print(f"ZNAJDŹ MNIE {type(allPaths)}")
    print(f"Number of roads found: {str(len(allPaths))}")
    allPaths, startEdges, stopEdges = changeToEdgesTable(
        allPaths, data[1], data[2], a, b
    )
    disjointRoads = findDisjointRoads(
        allPaths, k, timeLimit, roundLimit, startEdges, stopEdges
    )
    for i, road in enumerate(disjointRoads):
        print(f"Path nr: {str(i + 1)}/{str(k)}\n{road[0]}")
        print(f"Path weight is: {str(road[1])}\n")
    exactAlgorithmTime = round(time.time() - exactStart, roundLimit)
    print(f"----- Exact algorithm finished in: {str(exactAlgorithmTime)}\n")

    allProgramTime = round(time.time() - globalStart, roundLimit)
    print(f"Program finished in: {str(allProgramTime)}\n")

    print("--------------------------- Final Data ----------------------------")
    print(f"generateDataTime: {str(generateDataTime)}")
    print(f"dijkstraAlgorithmTime: {str(dijkstraAlgorithmTime)}")
    print(f"exactAlgorithmTime: {str(exactAlgorithmTime)}")
    print(f"allProgramTime: {str(allProgramTime)}")

    return [
        generateDataTime,
        dijkstraAlgorithmTime,
        allShortestPaths,
        allShortestPathsWeights,
        exactAlgorithmTime,
        disjointRoads,
        allProgramTime,
    ]
