from matplotlib import pyplot as plt

name="Long-n"

dijkstra_xs=[10,11,12,13,14,15,16,17,18,19,20,21]
dijkstra_ys=[53, 106, 216, 447, 970, 2024, 4204, 8890, 20032, 51111, 130524, 323850]

dial_xs=[10,11,16,17,18,19,20,21]
dial_ys=[1130, 25749, 2799, 5741, 14078, 8592, 18780, 45085]

plt.plot(dijkstra_xs, dijkstra_ys, label="Dijkstra")
plt.plot(dial_xs, dial_ys, label="Dial")
plt.title(name)
plt.xlabel("Graph index")
plt.ylabel("Time [ms]")
plt.legend()

plt.show()