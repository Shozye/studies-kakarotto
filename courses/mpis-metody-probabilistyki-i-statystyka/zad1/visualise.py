import os
import json
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import math


def make_function_from_parsed_data(function_name, parsed_data):
    x_axis = []
    y_axis = []
    for n in range(1000, 100001, 1000):
        key = str(n)
        value = parsed_data[key]
        x_axis.append(key)
        y_axis.append(value[function_name])
    return [x_axis, y_axis]


def parse_data(dir_name: str) -> dict:
    functions = dict()
    parsed_data = dict()
    for filename in os.listdir(os.path.join("logs", dir_name)):
        parsed_n_data = dict()
        with open(os.path.join("logs", dir_name, filename), "r") as file:
            data = json.loads(file.read())
            for k_try in data:
                for key, value in list(k_try["answers"].items()):
                    if parsed_n_data.get(key) is None:
                        parsed_n_data[key] = 0
                    parsed_n_data[key] += value
        for key, value in list(parsed_n_data.items()):
            parsed_n_data[key] = value / 50

        parsed_data[filename.split(".")[0]] = parsed_n_data

    for f_name in ["Bn", "Un", "Ln", "Cn", "Dn", "Dn__Minus__Cn"]:
        functions[f_name] = make_function_from_parsed_data(f_name, parsed_data)
    return functions


def make_multi_function_from_full_data(function_name, full_data):
    x_axis = []
    y_axis = []
    for n in range(1000, 100001, 1000):
        key = str(n)
        value = full_data[key]
        for k_try in value:
            x_axis.append(key)
            y_axis.append(k_try["answers"][function_name])
    return [x_axis, y_axis]


def get_full_data(dir_name):
    functions = dict()
    data_of_all_ns_and_their_ks = dict()
    for filename in os.listdir(os.path.join("logs", dir_name)):
        with open(os.path.join("logs", dir_name, filename), "r") as file:
            full_n_data = json.loads(file.read())
        data_of_all_ns_and_their_ks[filename.split(".")[0]] = full_n_data

    for f_name in ["Bn", "Un", "Ln", "Cn", "Dn", "Dn__Minus__Cn"]:
        functions[f_name] = make_multi_function_from_full_data(f_name, data_of_all_ns_and_their_ks)
    return functions


def get_title(function_name, title_name):
    titles = {"Bn": f"{title_name} : Birthday Paradox - Amount of balls needed to have 2 balls in 1 bin",
              "Un": f"{title_name} : Amount of empty bins after n balls",
              "Ln": f"{title_name} : Maximum Load after n balls",
              "Cn": f"{title_name} : Amount of balls after which there are no empty bins",
              "Dn": f"{title_name} : Amount of balls needed to every bin have 2 balls",
              "Dn__Minus__Cn": f"Dn-Cn : Difference between amount of balls needed to every bin have 2 balls and "
                               "amount of balls needed to every bin is not empty"}
    return titles[function_name]


def setup_plot_for_function(_ax, function_name, title_name=None):
    if title_name is None:
        title_name = function_name
    _ax.set(title=get_title(function_name, title_name))
    _ax.plot(average_data[function_name][0], average_data[function_name][1], '-ro', label=f'{function_name} average',
             ms=8)
    _ax.scatter(x=all_data[function_name][0], y=all_data[function_name][1], c='g', label=f'all f{function_name} data',
                s=5)
    _ax.legend()
    _ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    _ax.set_xlabel("Amount of bins - N")
    return _ax


def setup_average_plot_for_function(_ax, function_name, title_name=None, data=None):
    if title_name is None:
        title_name = function_name
    _ax.set(title=get_title(function_name, title_name))
    _ax.plot(average_data[function_name][0], data[function_name][1], '-ro', label=f'{title_name} average',
             ms=8)
    _ax.legend()
    _ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    _ax.set_xlabel("Amount of bins - N")
    return _ax


if __name__ == "__main__":
    dirname = "run_3"
    average_data = parse_data(dirname)
    all_data = get_full_data(dirname)
    with open("average_data_test.json", "w+") as file:
        file.write(json.dumps(average_data, indent=4))
    with open("all_data_test.json", "w+") as file:
        file.write(json.dumps(all_data, indent=4))

    fig, ax = plt.subplots(6, 1, figsize=(13, 20))
    for index, f_name in enumerate(["Bn", "Un", "Ln", "Cn", "Dn", "Dn__Minus__Cn"]):
        setup_plot_for_function(ax[index], f_name)
    fig.tight_layout()
    fig.show()
    fig.savefig("plot.png")

    average_data_bn_divided_n = parse_data(dirname)
    average_data_bn_divided_sqrt_n = parse_data(dirname)

    average_data_un_divided_n = parse_data(dirname)

    average_data_ln_divided_lnn = parse_data(dirname)
    average_data_ln_divided_lnn_divided_lnlnn = parse_data(dirname)
    average_data_ln_divided_lnlnn = parse_data(dirname)

    average_data_cn_divided_n = parse_data(dirname)
    average_data_cn_divided_nlnn = parse_data(dirname)
    average_data_cn_divided_nn = parse_data(dirname)

    average_data_dn_divided_n = parse_data(dirname)
    average_data_dn_divided_nlnn = parse_data(dirname)
    average_data_dn_divided_nn = parse_data(dirname)

    average_data_dn__Minus__cn_divided_n = parse_data(dirname)
    average_data_dn__Minus__cn_divided_nlnn = parse_data(dirname)
    average_data_dn__Minus__cn_divided_nlnlnn = parse_data(dirname)

    for n in range(1, 101):
        print(average_data_bn_divided_n["Bn"][1][n - 1])
        average_data_bn_divided_n["Bn"][1][n - 1] = average_data_bn_divided_n["Bn"][1][n - 1] / (n * 1000)
        average_data_bn_divided_sqrt_n["Bn"][1][n - 1] = average_data_bn_divided_sqrt_n["Bn"][1][n - 1] / math.sqrt(
            n * 1000)

        average_data_un_divided_n["Un"][1][n - 1] = average_data_un_divided_n["Un"][1][n - 1] / (n * 1000)

        average_data_ln_divided_lnn["Ln"][1][n - 1] = average_data_ln_divided_lnn["Ln"][1][n - 1] / math.log(n * 1000)
        average_data_ln_divided_lnn_divided_lnlnn["Ln"][1][n - 1] = average_data_ln_divided_lnn_divided_lnlnn["Ln"][1][
                                                                        n - 1] / (math.log(n * 1000) / math.log(
            math.log(n * 1000)))
        average_data_ln_divided_lnlnn["Ln"][1][n - 1] = average_data_ln_divided_lnlnn["Ln"][1][n - 1] / math.log(
            math.log(n * 1000))

        average_data_cn_divided_n["Cn"][1][n - 1] = average_data_cn_divided_n["Cn"][1][n - 1] / (n * 1000)
        average_data_cn_divided_nlnn["Cn"][1][n - 1] = average_data_cn_divided_nlnn["Cn"][1][n - 1] / (
                (n * 1000) * math.log(n * 1000))
        average_data_cn_divided_nn["Cn"][1][n - 1] = average_data_cn_divided_nn["Cn"][1][n - 1] / (n * 1000 * n * 1000)

        average_data_dn_divided_n["Dn"][1][n - 1] = average_data_dn_divided_n["Dn"][1][n - 1] / (n * 1000)
        average_data_dn_divided_nlnn["Dn"][1][n - 1] = average_data_dn_divided_nlnn["Dn"][1][n - 1] / (
                (n * 1000) * math.log(n * 1000))
        average_data_dn_divided_nn["Dn"][1][n - 1] = average_data_dn_divided_nn["Dn"][1][n - 1] / (n * 1000 * n * 1000)

        average_data_dn__Minus__cn_divided_n["Dn__Minus__Cn"][1][n - 1] = \
            average_data_dn__Minus__cn_divided_n["Dn__Minus__Cn"][1][n - 1] / (n * 1000)
        average_data_dn__Minus__cn_divided_nlnn["Dn__Minus__Cn"][1][n - 1] = \
            average_data_dn__Minus__cn_divided_nlnn["Dn__Minus__Cn"][1][n - 1] / ((n * 1000) * math.log(n * 1000))
        average_data_dn__Minus__cn_divided_nlnlnn["Dn__Minus__Cn"][1][n - 1] = \
            average_data_dn__Minus__cn_divided_nlnlnn["Dn__Minus__Cn"][1][n - 1] / (
                    (n * 1000) * math.log(math.log(n * 1000)))

    plt.clf()
    fig, ax = plt.subplots(2, 1, figsize=(13, 8))
    f_name = "Bn"
    setup_average_plot_for_function(ax[0], f_name, f"{f_name}/n", average_data_bn_divided_n)
    setup_average_plot_for_function(ax[1], f_name, f"{f_name}/sqrt(n)", average_data_bn_divided_sqrt_n)
    fig.tight_layout()
    fig.show()
    fig.savefig(f"plot_{f_name}_variations.png")

    fig, ax = plt.subplots(1, 1, figsize=(13, 4))
    f_name = "Un"
    setup_average_plot_for_function(ax, f_name, f"{f_name}/n", average_data_un_divided_n)
    fig.tight_layout()
    fig.show()
    fig.savefig(f"plot_{f_name}_variations.png")

    fig, ax = plt.subplots(3, 1, figsize=(13, 12))
    f_name = "Ln"
    setup_average_plot_for_function(ax[0], f_name, f"{f_name}/ln(n)", average_data_ln_divided_lnn)
    setup_average_plot_for_function(ax[1], f_name, f"{f_name}/( ln(n)/ln(ln(n)) )",
                                    average_data_ln_divided_lnn_divided_lnlnn)
    setup_average_plot_for_function(ax[2], f_name, f"{f_name}/ln(ln(n))", average_data_ln_divided_lnlnn)
    fig.tight_layout()
    fig.show()
    fig.savefig(f"plot_{f_name}_variations.png")

    fig, ax = plt.subplots(3, 1, figsize=(13, 12))
    f_name = "Cn"
    setup_average_plot_for_function(ax[0], f_name, f"{f_name}/n", average_data_cn_divided_n)
    setup_average_plot_for_function(ax[1], f_name, f"{f_name}/( n*ln(n) )", average_data_cn_divided_nlnn)
    setup_average_plot_for_function(ax[2], f_name, f"{f_name}/n^2)", average_data_cn_divided_nn)
    fig.tight_layout()
    fig.show()
    fig.savefig(f"plot_{f_name}_variations.png")

    fig, ax = plt.subplots(3, 1, figsize=(13, 12))
    f_name = "Dn"
    setup_average_plot_for_function(ax[0], f_name, f"{f_name}/n", average_data_dn_divided_n)
    setup_average_plot_for_function(ax[1], f_name, f"{f_name}/( n*ln(n) )", average_data_dn_divided_nlnn)
    setup_average_plot_for_function(ax[2], f_name, f"{f_name}/n^2)", average_data_dn_divided_nn)
    fig.tight_layout()
    fig.show()
    fig.savefig(f"plot_{f_name}_variations.png")

    fig, ax = plt.subplots(3, 1, figsize=(13, 12))
    f_name = "Dn__Minus__Cn"
    setup_average_plot_for_function(ax[0], f_name, f"{f_name}/n", average_data_dn__Minus__cn_divided_n)
    setup_average_plot_for_function(ax[1], f_name, f"{f_name}/( n*ln(n) )", average_data_dn__Minus__cn_divided_nlnn)
    setup_average_plot_for_function(ax[2], f_name, f"{f_name}/n*ln(ln(n))", average_data_dn__Minus__cn_divided_nlnlnn)
    fig.tight_layout()
    fig.show()
    fig.savefig(f"plot_{f_name}_variations.png")
