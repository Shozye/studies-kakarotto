import json
import os
import matplotlib.pyplot as plt


def parse_data(log):
    return_data = dict()
    Lnfunctions = dict()
    Lnmultifunctions = dict()

    for d in range(1, 4):
        Lnfunctions[d] = [[], []]
        Lnmultifunctions[d] = [[], []]

    for n in range(1000, 100001, 1000):
        for d in range(1, 4):

            d_average_value = 0
            d_all_k_simulation_values = []
            amount_of_different_d_simulation_runs = 0
            n_data = log[str(n)]
            for k_simulation_run in n_data:
                if d == k_simulation_run["d"]:
                    d_average_value += k_simulation_run["Ln"]
                    d_all_k_simulation_values.append(k_simulation_run["Ln"])
                    amount_of_different_d_simulation_runs += 1
            d_average_value /= amount_of_different_d_simulation_runs

            Lnfunctions[d][0].append(n)
            Lnfunctions[d][1].append(d_average_value)

            Lnmultifunctions[d][0].extend([n] * len(d_all_k_simulation_values))
            Lnmultifunctions[d][1].extend(d_all_k_simulation_values)

    return_data["functions"] = Lnfunctions
    return_data["multifunctions"] = Lnmultifunctions
    return return_data


def get_title(_f_name, _title_name):
    f_name = "d" + str(_f_name)
    titles = {"d1": f"{_title_name} - Maximum load for ballanced allocation d = 1",
              "d2": f"{_title_name} - Maximum load for ballanced allocation d = 2",
              "d3": f"{_title_name} - Maximum load for ballanced allocation d = 3"}
    return titles[f_name]


def setup_plot(_ax, _f_name, data, title_name=None, function=False, multifunction=False):
    if title_name is None:
        title_name = _f_name
    _ax.set(title=get_title(_f_name, title_name))
    if function:
        f = data["functions"][_f_name]
        _ax.plot(f[0], f[1], 'ro', label=f"d={str(_f_name)} average", ms=8)
    if multifunction:
        mf = data["multifunctions"][_f_name]
        _ax.scatter(x=mf[0], y=mf[1], c='g', label=f"all d={str(_f_name)} data", s=7)
    _ax.legend()
    _ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    _ax.set_xlabel("Length of permutation - N")


def main(plot_dirname, data_dirname):
    with open(os.path.join("logs", data_dirname, "full_log.json")) as file:
        full_log = json.loads(file.read())
    parsed_data = parse_data(full_log)

    if not os.path.isdir(plot_dirname):
        os.mkdir(plot_dirname)

    fig, ax = plt.subplots(3, 1, figsize=(13, 12))
    for d in range(1, 4):
        setup_plot(ax[d - 1], d, parsed_data, None, True, True)
    fig.tight_layout()
    fig.show()
    fig.savefig(os.path.join(plot_dirname, "Ln_plot_d_1_to_4.png"))


if __name__ == "__main__":
    main("plots", "run_4")
