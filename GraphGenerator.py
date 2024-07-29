import random
import time
from typing import List, Tuple


def generateGraphData(
    N: int, a: float, b: float, roundLimit: int
) -> List[List[Tuple[int, int]]]:
    start = time.time()
    print("Start generating graph data...")
    nodes = []
    edgesWithWeight = []
    for i in range(N):
        for j in range(N):
            nodes.append((i, j))
            if i < N - 1 and j < N - 1:
                edgesWithWeight.append(
                    ((i, j), (i, j + 1), round(random.uniform(a, b), 1))
                )
                edgesWithWeight.append(
                    ((i, j), (i + 1, j + 1), round(random.uniform(a, b), 1))
                )
                edgesWithWeight.append(
                    ((i, j), (i + 1, j), round(random.uniform(a, b), 1))
                )
            else:
                if i < N - 1 and j == N - 1:
                    edgesWithWeight.append(
                        ((i, j), (i + 1, j), round(random.uniform(a, b), 1))
                    )
                if i == N - 1 and j < N - 1:
                    edgesWithWeight.append(
                        ((i, j), (i, j + 1), round(random.uniform(a, b), 1))
                    )
            if i < N - 1 and j > 0:
                edgesWithWeight.append(
                    ((i, j), (i + 1, j - 1), round(random.uniform(a, b), 1))
                )
    edgesTable = [[i, edge[2]] for i, edge in enumerate(edgesWithWeight)]
    print(f"Graph data generated in: {round(time.time() - start, roundLimit)}\n")
    return [nodes, edgesWithWeight, edgesTable]
