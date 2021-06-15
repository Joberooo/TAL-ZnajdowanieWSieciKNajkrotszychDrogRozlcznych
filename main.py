from RunProgram import runSingleProgram


def main():
    # data[i] = [N, k, A, B, minWeight, maxWeight, timeLimit, roundLimit]
    k = 3
    data = [
        [2, k, (0, 0), (1, 1), 1.0, 9.0, 1000, 5],
        [3, k, (0, 0), (2, 2), 1.0, 9.0, 1000, 5],
        [4, k, (0, 0), (3, 3), 1.0, 9.0, 1000, 5]
    ]
    runSingleProgram(data, k)

    k = 8
    data = [
        [2, k, (0, 0), (1, 1), 1.0, 9.0, 1000, 5],
        [3, k, (0, 0), (2, 2), 1.0, 9.0, 1000, 5],
        [4, k, (0, 0), (3, 3), 1.0, 9.0, 1000, 5]
    ]
    runSingleProgram(data, k)

    data = [
        [4, k, (1, 1), (2, 2), 1.0, 9.0, 1000, 5],
        [5, k, (1, 1), (3, 3), 1.0, 9.0, 1000, 5]
    ]
    runSingleProgram(data, k)


if __name__ == '__main__':
    main()
