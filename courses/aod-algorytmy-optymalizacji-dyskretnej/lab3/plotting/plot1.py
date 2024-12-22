from matplotlib import pyplot as plt

name="Random4-n"

dijkstra_xs=[10,11,12,13,14,15,16,17,18,19,20,21]
dijkstra_ys=[77, 160, 345, 776, 1724, 3688, 7860, 17550, 40995, 116639, 300343, 668512]

dial_xs=[10,11,12,16,17,19,20]
dial_ys=[1263, 24313, 95328, 3671, 8528, 57039, 128061]

plt.plot(dijkstra_xs, dijkstra_ys, label="Dijkstra")
plt.plot(dial_xs, dial_ys, label="Dial")
plt.title("Random4-n")
plt.xlabel("Graph index")
plt.ylabel("Time [ms]")
plt.legend()

plt.show()