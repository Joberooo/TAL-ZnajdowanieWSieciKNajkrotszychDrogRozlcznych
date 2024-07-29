# Finding k Shortest Edge-Disjoint Paths in a Network

The problem of finding edge-disjoint paths involves determining possible paths from point **A** to point **B** in a graph such that each path does not reuse any edge. In the context of this project, the task is to find the **k** possible number of shortest paths between points in such a way that the paths are disjoint and shortest.

## Algorithm Description

In this project, the task of finding k shortest edge-disjoint paths is accomplished using both the Exact Algorithm and Dijkstra's algorithm.

### Exact Algorithm

The exact algorithm works by:

1. Determining all possible paths from point A to point B without considering their disjointness and length.
2. Storing these paths in a table.
3. Checking each possible combination of paths for disjointness.
4. Recording combinations of paths that meet the disjointness condition and are the shortest.

### Modified Dijkstra's Algorithm

The modified Dijkstra's algorithm for finding k shortest paths works by:

1. Finding the shortest path in the graph.
2. Removing this path from the graph.
3. Repeating the process until k shortest paths are found.

## Setup Instructions

### Requirements

- `networkx` library
- `numpy` library
- `random` library

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Joberooo/TAL-ZnajdowanieWSieciKNajkrotszychDrogRozlcznych.git
   cd TAL-ZnajdowanieWSieciKNajkrotszychDrogRozlcznych
   ```

2. Install the required libraries:
   ```bash
   pip install networkx numpy
   ```

## Running the Code

1. Ensure all scripts are in the appropriate directories within the project folder.
2. Run the main script which includes data generation and both algorithm executions:
   ```bash
   python main.py
   ```

## Example Usage

The `main.py` script includes predefined data and runs both the exact and Dijkstra's algorithms:

```python
# data[i] = [N, k, A, B, minWeight, maxWeight, timeLimit, roundLimit]
k = 3
data = [
    [2, k, (0, 0), (1, 1), 1.0, 9.0, 1000, 5],
    [3, k, (0, 0), (2, 2), 1.0, 9.0, 1000, 5],
    [4, k, (0, 0), (3, 3), 1.0, 9.0, 1000, 5],
]
runSingleProgram(data, k)
```

Each element in the data table represents a set of parameters for the graph and algorithms:

- **`N`**: Dimension of the graph (NxN).
- **`k`**: Number of shortest paths to find.
- **`A`**: Starting vertex (tuple of coordinates, e.g., (0, 0)).
- **`B`**: Ending vertex (tuple of coordinates, e.g., (1, 1)).
- **`minWeight`**: Minimum weight of the edges.
- **`maxWeight`**: Maximum weight of the edges.
- **`timeLimit`**: Time limit for the exact algorithm.
- **`roundLimit`**: Limit on the number of rounds for the exact algorithm.
