import json
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import math
figure(figsize=(5.3, 5.3), dpi=80)


PLOTS = "plots.png"
DATA = "data.json"
with open(DATA, 'r') as file:
    data = json.loads(file.read())

Xs = data["Xs"]
comparisons = data["comparisons"]
displacements = data["displacements"]
LINEWIDTH=10
plt.plot(Xs, comparisons, label="comparisons", color="darkred", linewidth=LINEWIDTH)
plt.plot(Xs, displacements, label="displacements", color="darkblue", linewidth=LINEWIDTH)

plt.plot(Xs, [0.8*x*x for x in Xs], color='pink', label="y=0.8 * x^2", linewidth=LINEWIDTH/4)
plt.plot(Xs, [2.2*x*x for x in Xs], color='lime', label="y=2.2 * x^2", linewidth=LINEWIDTH/4)
plt.title("Complexity Research - LCS algorithm")
plt.xlabel("N - Amount of numbers")
plt.ylabel("Amount of operations")
plt.legend()
plt.tight_layout()
plt.savefig(PLOTS)
plt.clf()