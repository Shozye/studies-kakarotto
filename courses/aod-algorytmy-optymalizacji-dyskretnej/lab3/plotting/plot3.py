from matplotlib import pyplot as plt

name="Square-n"

dijkstra_xs=[10,11,12,13,14,15,16,17,18,19,20,21]
dijkstra_ys=[57, 117, 250, 549, 1208, 2606, 6133, 13667, 30392, 88282, 216492, 473636]

dial_xs=[16,18,19]
dial_ys=[2800, 15472, 19022]

plt.plot(dijkstra_xs, dijkstra_ys, label="Dijkstra")
plt.plot(dial_xs, dial_ys, label="Dial")
plt.title(name + " -ss")
plt.xlabel("Graph index")
plt.ylabel("Time [ms]")
plt.legend()

plt.show()