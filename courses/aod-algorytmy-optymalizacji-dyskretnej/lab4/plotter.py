import os
from collections import defaultdict
from matplotlib import pyplot as plt
import json

def avg(nums):
    return sum(nums) / len(nums)

def make_plot(X, Y, title, filename):
    plt.plot(X, Y)
    plt.title(title)
    plt.savefig(os.path.join("plots", filename))
    plt.clf()
    
def make_zad1_plots():
    plot_data = dict()
    
    datadir = "zad1_data"
    for filename in os.listdir(datadir):
        num = int(filename[:-4])
        filepath = os.path.join(datadir, filename)
        
        times = []
        max_flows = []
        amount_augmented = []
        with open(filepath) as file:
            lines = file.read()
            for line in lines.split("\n")[:-1]:
                splitted = line.split(":")
                times.append(int(splitted[2]))
                max_flows.append(int(splitted[6]))
                amount_augmented.append(int(splitted[4]))
        plot_data[num] = {
            "avg_time": avg(times),
            "avg_max_flow": avg(max_flows),
            "avg_augments": avg(amount_augmented)
        }
    
    with open("dump.json", 'w+') as file:
        file.write(json.dumps(plot_data, indent=4, sort_keys=True))
        
    X = list(range(1,17))

    Y_time = [plot_data[x]["avg_time"] for x in X]
    Y_max_flow = [plot_data[x]["avg_max_flow"] for x in X]
    Y_augments = [plot_data[x]["avg_augments"] for x in X]
    
    make_plot(X, Y_time, "Average time", "time.png")
    make_plot(X, Y_max_flow, "Average flow", "flow.png")
    make_plot(X, Y_augments, "Average amount of augments", "augments.png")

    
def make_zad2_plots():
    plot_data = defaultdict(dict)
    datadir = "zad2_data"
    os.makedirs("zad2_plots", exist_ok=True)
    for filename in os.listdir(datadir):
        k=int(filename.split("_")[1])
        degree=int(filename.split("_")[3])
        
        times = []
        max_flows = []
        
        with open(os.path.join(datadir, filename)) as file:  
            lines = file.read().split("\n")[:-1]
        for line in lines:
            splitted = line.split(":")
            
            times.append(int(splitted[2]))
            max_flows.append(int(splitted[6]))
        
        plot_data[k][degree] = {
            "avg_time": avg(times),
            "avg_max_flow": avg(max_flows),
        }
    
    for i in range(1, 11):
        y_time = []
        x = 20
        for k in range(3, 11):
            if i in plot_data[k]:
                x = min(x, k)
                y_time.append(plot_data[k][i]["avg_time"])
        X = list(range(x, x+len(y_time)))
        plt.plot(X, y_time, label=f"i={i}")
        plt.scatter(X, y_time)
    plt.legend()
    plt.title("Time of execution for k and i in bipartite problem")
    plt.xlabel("k")
    plt.ylabel("time[ms]")
    plt.savefig("zad2_plots/time.png")
    plt.clf()

    with open("dump2.json", 'w+') as file:
        file.write(json.dumps(plot_data, indent=4, sort_keys=True))
    
    for i in range(1, 11):
        y_max_flow = []
        x = 20
        for k in range(3, 11):
            if i in plot_data[k]:
                x = min(x, k)
                y_max_flow.append(plot_data[k][i]["avg_max_flow"])
        X = list(range(x, x+len(y_max_flow)))
        plt.plot(X, y_max_flow, label=f"i={i}")
        plt.scatter(X, y_max_flow)
    plt.legend()
    plt.yticks([32,64,128,256,512,1024])
    plt.grid()
    plt.title("Average maximal flow Maximal flow for k and i in bipartite problem")
    plt.xlabel("k")
    plt.savefig("zad2_plots/max_flow.png")

    plt.clf()    

def main():
    make_zad1_plots()
    make_zad2_plots()

if __name__ == "__main__":
    main()