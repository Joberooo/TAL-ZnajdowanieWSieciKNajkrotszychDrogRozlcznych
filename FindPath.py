import networkx as nx
import time
from typing import List, Tuple


def takeSecond(elem):
    return elem[1]


def findAllSimplePaths(
    graph: nx.Graph,
    source: int,
    target: int,
    data: List[Tuple[int, int, float]],
    roundLimit: int,
) -> List[List[int]]:
    start = time.time()
    print("Start searching for all paths...")
    allPaths = nx.all_simple_paths(graph, source=source, target=target)
    allPathsTable = [
        [path, round(calcPathWeightWithoutPrint(data, path), 2)] for path in allPaths
    ]
    allPathsTable.sort(key=takeSecond)
    print(f"All paths found in: {round(time.time() - start, roundLimit)}\n")
    return allPathsTable


def findAllShortestPathsDijkstra(
    graph: nx.Graph, source: int, target: int, k: int, roundLimit: int
) -> List[List[int]]:
    start = time.time()
    print("Start searching for all the shortest paths (Dijkstra)...")
    pathsTable = []
    for i in range(k):
        try:
            start2 = time.time()
            x = nx.dijkstra_path(graph, source, target, weight="weight")
            pathsTable.append(x)
            for j in range(len(x) - 1):
                graph.remove_edge(x[j], x[j + 1])
            print(
                f"Path number: {i + 1}/{k} found (Dijkstra) in: {round(time.time() - start2, roundLimit)}..."
            )
        except nx.NetworkXNoPath:
            print("No next shortest path from point A to point B (Dijkstra)")
            break
    print(
        f"All shortest paths by Dijkstra found in: {round(time.time() - start, roundLimit)}\n"
    )
    return pathsTable


def calcPathWeight(weightTable: List[Tuple[int, int, float]], way: List[int]) -> float:
    start = time.time()
    print("Start calculating path weight...")
    summary = calcPathWeightWithoutPrint(weightTable, way)
    print(f"Path weight is: {round(summary, 1)}")
    print(f"Calculation finished in: {round(time.time() - start, 3)}\n")
    return summary


def calcPathWeightWithoutPrint(
    weightTable: List[Tuple[int, int, float]], way: List[int]
) -> float:
    summary = 0
    for i in range(len(way) - 1):
        for j in range(len(weightTable)):
            if (way[i], way[i + 1]) == (weightTable[j][0], weightTable[j][1]) or (
                way[i + 1],
                way[i],
            ) == (weightTable[j][0], weightTable[j][1]):
                summary += weightTable[j][2]
    return summary


def changeToEdgesTable(
    allPaths: List[List[int]],
    data: List[Tuple[int, int, float]],
    edges: List[Tuple[int]],
    start: int,
    stop: int,
) -> Tuple[List[List[int]], List[int], List[int]]:
    allPaths2 = []
    startEdges = []
    stopEdges = []
    for path in allPaths:
        summary = 0
        onePath = []
        for i in range(len(path[0]) - 1):
            for j in range(len(data)):
                if (path[0][i], path[0][i + 1]) == (data[j][0], data[j][1]) or (
                    path[0][i + 1],
                    path[0][i],
                ) == (data[j][0], data[j][1]):
                    if (path[0][i]) == start:
                        exist = False
                        for z in startEdges:
                            if z == edges[j][0]:
                                exist = True
                        if not exist:
                            startEdges.append(edges[j][0])
                    if (path[0][i + 1]) == stop:
                        exist = False
                        for z in stopEdges:
                            if z == edges[j][0]:
                                exist = True
                        if not exist:
                            stopEdges.append(edges[j][0])
                    summary += data[j][2]
                    onePath.append(edges[j][0])
                    break
        allPaths2.append([onePath, round(summary, 2)])
    return allPaths2, startEdges, stopEdges


def findDisjointRoads(
    allPaths: List[List[int]],
    k: int,
    timeLimit: int,
    roundLimit: int,
    startEdges: List[int],
    stopEdges: List[int],
) -> List[List[int]]:
    start = time.time()
    print("Start finding disjoint roads...")
    disjointRoads = [allPaths[0]]
    for i in allPaths[0][0]:
        for j in startEdges:
            if i == j:
                startEdges.remove(i)
        for j in stopEdges:
            if i == j:
                stopEdges.remove(i)

    while len(disjointRoads) < k:
        if len(startEdges) == 0 or len(stopEdges) == 0:
            print("\nNo more roads!")
            print("!--------------------------- BREAK ---------------------------!\n")
            break
        for simplePath in allPaths:
            goNext = True
            for joinedPath in disjointRoads:
                if simplePath[0] == joinedPath[0]:
                    goNext = False
                    break
            if goNext:
                allWays = []
                for joinedPath in disjointRoads:
                    for element in joinedPath[0]:
                        allWays.append(element)
                add = True
                for element in simplePath[0]:
                    for elementTwo in allWays:
                        if element == elementTwo:
                            add = False
                if add:
                    disjointRoads.append(simplePath)
                    for i in simplePath[0]:
                        for j in startEdges:
                            if i == j:
                                startEdges.remove(i)
                        for j in stopEdges:
                            if i == j:
                                stopEdges.remove(i)
        if (time.time() - start) > timeLimit:
            print("\nTime limit has been reached!")
            print("!--------------------------- BREAK ---------------------------!\n")
            break

    print(f"DisjointRoads found in: {round(time.time() - start, roundLimit)}\n")
    return disjointRoads
