from matplotlib import pyplot as plt
import json
import sys

def visualise(filepath: str):
    with open(filepath, 'r') as file:
        data = json.loads(file.read())
    Xs = sorted(data['Xs'])
    rsa_time_values = sorted(data["rsa_time_values"])
    rsa_crt_time_values = sorted(data["rsa_crt_time_values"])

    plt.plot(Xs, rsa_time_values, label="Rsa")
    plt.plot(Xs, rsa_crt_time_values, label="Rsa CRT")
    plt.xlabel("Size of input in bits")
    plt.ylabel("Time needed per prime pair [s]")
    plt.tight_layout()
    plt.legend()
    plt.show()

def visualise_with_estimations(filepath: str):
    with open(filepath, 'r') as file:
        data = json.loads(file.read())
    Xs = sorted(data['Xs'])
    XsForEstimation = list(range(128, 4097, 2))
    rsa_time_values = sorted(data["rsa_time_values"])
    rsa_crt_time_values = sorted(data["rsa_crt_time_values"])

    plots = [
        [Xs, rsa_time_values, "RSA", 5],
        [Xs, rsa_crt_time_values, "RSA CRT", 5],
        [XsForEstimation, [1/(2**27 * 2.25)*x**3 for x in XsForEstimation], f"1/{round((2**27 * 2.25))} * x^3", 2],
        [XsForEstimation, [1/(2**25 * 2.5)*x**3 for x in XsForEstimation], f"1/{round((2**25 * 2.5))} * x^3", 2]
    ]

    for X, values, label, linewidth in plots:
        plt.plot(X, values, label=label, linewidth=linewidth)
    plt.xlabel("n - Size of input in bits")
    plt.ylabel("t - Time needed per prime pair [s]")
    plt.tight_layout()
    plt.legend()
    plt.savefig("plot.png")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) == 1 and sys.argv[1] == "--additional":
        visualise_with_estimations("plot_data.json")
    else:
        visualise("plot_data.json")