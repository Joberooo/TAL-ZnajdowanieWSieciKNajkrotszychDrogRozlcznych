import random
import time


def generateGraphData(N, a, b, roundLimit):
    start = time.time()
    print("Start generating graph data...")
    nodes = []
    edgesWithWeight = []
    for i in range(N):
        for j in range(N):
            nodes.append((i, j))
            if i < N - 1 and j < N - 1:
                edgesWithWeight.append(((i, j), (i, j + 1), round(random.uniform(a, b), 1)))
                edgesWithWeight.append(((i, j), (i + 1, j + 1), round(random.uniform(a, b), 1)))
                edgesWithWeight.append(((i, j), (i + 1, j), round(random.uniform(a, b), 1)))
            else:
                if i < N - 1 and j == N - 1:
                    edgesWithWeight.append(((i, j), (i + 1, j), round(random.uniform(a, b), 1)))
                if i == N - 1 and j < N - 1:
                    edgesWithWeight.append(((i, j), (i, j + 1), round(random.uniform(a, b), 1)))
            if i < N - 1 and j > 0:
                edgesWithWeight.append(((i, j), (i + 1, j - 1), round(random.uniform(a, b), 1)))
    edgesTable = []
    i = 0
    for edge in edgesWithWeight:
        edgesTable.append([i, edge[2]])
        i += 1
    print("Graph data generated in: " + str(round(time.time() - start, roundLimit)) + "\n")
    return [nodes, edgesWithWeight, edgesTable]
