from matplotlib import pyplot as plt
from typing import List


def drawPlot(
    data_line: List[int],
    generate_data_time: List[float],
    dijkstra_time: List[float],
    exact_time: List[float],
    all_program_time: List[float],
    k: int,
) -> None:
    plt.plot(data_line, generate_data_time, "r--", label="generateDataTime")
    plt.plot(data_line, dijkstra_time, "y-.", label="dijkstraTime")
    plt.plot(data_line, exact_time, "b:", label="exactTime")
    plt.plot(data_line, all_program_time, "k", label="allProgramTime")
    title_text = "Times from the dimension N for k = " + str(k)
    plt.gca().set(ylabel="Time", xlabel="N", title=title_text)
    plt.legend()
    plt.show()
