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

# plt.plot(Xs, [39*x for x in Xs], color='yellow', label='y=37x', linewidth=LINEWIDTH/4)
# plt.plot(Xs, [58*x for x in Xs], color='orange', label='y=56x', linewidth=LINEWIDTH/4)
plt.plot(Xs, [4.2*math.log(x)*x for x in Xs], color='violet', label="y=4.2xlogx", linewidth=LINEWIDTH/4)
plt.plot(Xs, [2.8*math.log(x)*x for x in Xs], color='lime', label="y=2.8xlogx", linewidth=LINEWIDTH/4)
plt.title("Complexity research: insert all then extract all - HEAP")
plt.xlabel("N - Amount of numbers")
plt.ylabel("Amount of operations")
plt.legend()
plt.tight_layout()
plt.savefig(PLOTS)
plt.clf()