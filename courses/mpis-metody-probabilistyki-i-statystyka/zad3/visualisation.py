import os
import matplotlib.pyplot as plt
import json


def parse_function_from_parsed_data(parsed_data, function_name):
    x_axis = []
    y_axis = []
    for n in range(100, 10001, 100):
        x_axis.append(n)
        y_axis.append(parsed_data[n]["average_answers"][function_name])
    return [x_axis, y_axis]


def parse_multifunction_from_parsed_data(parsed_data, function_name):
    x_axis = []
    y_axis = []
    for n in range(100, 10001, 100):
        x_axis.extend(parsed_data[n]["x_axis"])
        y_axis.extend(parsed_data[n]["all_answers"][function_name])
    return [x_axis, y_axis]


def parse_data(dir_name: str) -> dict:
    return_data = dict()
    functions = dict()
    multifunctions = dict()
    parsed_data = dict()
    for filename in os.listdir(os.path.join("logs", dir_name)):
        n = int(filename.split(".")[0])
        parsed_n_data = dict()
        parsed_n_data["n"] = n
        parsed_n_data["average_answers"] = {"cmp": 0, "swp": 0, "time": 0}
        parsed_n_data["all_answers"] = {"cmp": list(), "swp": list(), "time": list()}
        with open(os.path.join("logs", dir_name, filename), "r") as file:
            data = json.loads(file.read())
        print(json.dumps(data, indent=4))

        k = len(data[0]["answers"])
        print("what is len of data:", k)
        parsed_n_data["x_axis"] = [n] * k
        for k_try in data[0]["answers"]:
            parsed_n_data["average_answers"]["cmp"] += k_try["cmp"]
            parsed_n_data["average_answers"]["swp"] += k_try["swp"]
            parsed_n_data["average_answers"]["time"] += k_try["time"]
            parsed_n_data["all_answers"]["cmp"].append(k_try["cmp"])
            parsed_n_data["all_answers"]["swp"].append(k_try["swp"])
            parsed_n_data["all_answers"]["time"].append(k_try["time"])
        parsed_n_data["average_answers"]["cmp"] /= k
        parsed_n_data["average_answers"]["swp"] /= k
        parsed_n_data["average_answers"]["time"] /= k
        parsed_data[n] = parsed_n_data

    for f_name in ["cmp", "swp", "time"]:
        functions[f_name] = parse_function_from_parsed_data(parsed_data, f_name)
        multifunctions[f_name] = parse_multifunction_from_parsed_data(parsed_data, f_name)

    return_data["functions"] = functions
    return_data["multifunctions"] = multifunctions
    return return_data


def get_title(_f_name, _title_name):
    titles = {"cmp": f"{_title_name} : Amount of comparisions needed to sort array",
              "time": f"{_title_name} : Amount of time needed to sort array",
              "swp": f"{_title_name} : Amount of inserts till sorted array"}
    return titles[_f_name]


def setup_plot(_ax, _f_name, data, title_name=None, function=False, multifunction=False):
    if title_name is None:
        title_name = _f_name
    _ax.set(title=get_title(_f_name, title_name))
    if function:
        function = data["functions"][_f_name]
        _ax.plot(function[0], function[1], 'ro', label=f"{_f_name} average", ms=8)
    if multifunction:
        multifunction = data["multifunctions"][_f_name]
        _ax.scatter(x=multifunction[0], y=multifunction[1], c='g', label=f"all {_f_name} data", s=7)
    _ax.legend()
    _ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    _ax.set_xlabel("Length of permutation - N")


def main(figure_logs_dir, figure_prefixes, dirname):
    if not os.path.isdir(figure_logs_dir):
        os.mkdir(figure_logs_dir)
    data = parse_data(dirname)
    fig, ax = plt.subplots(3, 1, figsize=(13, 12))
    for index, f_name in enumerate(["cmp", "swp", "time"]):
        setup_plot(ax[index], f_name, data, function=True, multifunction=True)
    fig.tight_layout()
    fig.show()
    fig.savefig(os.path.join(figure_logs_dir, figure_prefixes + "_plot.png"))

    average_data_cmp_divided_by_n = parse_data(dirname)
    average_data_cmp_divided_by_nn = parse_data(dirname)

    average_data_swp_divided_by_n = parse_data(dirname)
    average_data_swp_divided_by_nn = parse_data(dirname)

    for n in range(1, 1 + len(data["functions"]["cmp"][1])):
        average_data_cmp_divided_by_n["functions"]["cmp"][1][n - 1] /= (n * 100)
        average_data_cmp_divided_by_nn['functions']["cmp"][1][n - 1] /= (n * 100 * n * 100)

    for n in range(1, 1 + len(data["functions"]["swp"][1])):
        average_data_swp_divided_by_n["functions"]["swp"][1][n - 1] /= (n * 100)
        average_data_swp_divided_by_nn['functions']["swp"][1][n - 1] /= (n * 100 * n * 100)

    fig, ax = plt.subplots(2, 1, figsize=(13, 8))
    setup_plot(ax[0], "cmp", average_data_cmp_divided_by_n, "cmp/n", True, False)
    setup_plot(ax[1], "cmp", average_data_cmp_divided_by_nn, "cmp/n^2", True, False)
    fig.tight_layout()
    fig.show()
    fig.savefig(os.path.join(figure_logs_dir, figure_prefixes + "_plot_cmp_variations.png"))

    fig, ax = plt.subplots(2, 1, figsize=(13, 8))
    setup_plot(ax[0], "swp", average_data_swp_divided_by_n, "swp/n", True, False)
    setup_plot(ax[1], "swp", average_data_swp_divided_by_nn, "swp/n^2", True, False)
    fig.tight_layout()
    fig.show()
    fig.savefig(os.path.join(figure_logs_dir, figure_prefixes + "_plot_swp_variations.png"))


if __name__ == "__main__":
    main("plots", "k=10", "run_1")
    main("plots", "k=1", "run_2")
