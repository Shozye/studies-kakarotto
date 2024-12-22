import os
import shutil
from typing import List
from matplotlib import pyplot as plt

def main():
    M = 100 # Amount of files per N
    DATA = "data"
    PLOTS = "PLOTS"
    selects = ["random_select", "select"]
    gen_types = ["gen_asc", "gen_desc", "gen_rand"]
    
    if PLOTS in os.listdir():  # If plots directory exist in current directory
        shutil.rmtree(PLOTS)   # Delete it
    os.mkdir(PLOTS)            # Make new 
    
    for gen_type in gen_types:
        axs: List[List[plt.Axes]]
        fig: plt.Figure
        fig, axs = plt.subplots(3, 2, figsize=(20, 30))
        for select_type in selects:
            k_num=-1
            for k in ["first", "quarter", "half"]:
                k_num+=1
                data_path = os.path.join(DATA, select_type, gen_type, k)
                
                comparisons = dict()
                displacements = dict()
                
                for filename in os.listdir(data_path):
                    n = int(filename.split("_")[1])
                    
                    path_to_file = os.path.join(data_path, filename)
                    with open(path_to_file, 'r') as file:
                        # [:-1] means that we read all file except last letter which is '\n'
                        am_comparisons, am_displacements = list(map(int, file.read()[:-1].split(" ")))
                        
                    if comparisons.get(n) is None: comparisons[n] = 0
                    if displacements.get(n) is None: displacements[n] = 0
                    displacements[n] += am_displacements
                    comparisons[n] += am_comparisons
                
                for key in comparisons.keys():
                    comparisons[key] /= M
                    displacements[key] /= M
            
                
                Xs  = sorted(list(comparisons.keys()))
                YsC = [comparisons[x] for x in Xs]
                YsD = [displacements[x] for x in Xs]
                
                #XsLine = [Xs[0], Xs[-1]]
                #YsCLine = [YsC[0], YsC[-1]]
                #YsDLine = [YsD[0], YsD[-1]]
                
                LINEWIDTH = 3
                axs[k_num][0].plot(Xs, YsC, label=f"Comparisons {select_type}", linewidth=LINEWIDTH)
                #axs[k_num][0].plot(XsLine, YsCLine, linewidth=1, color='red')
                
                axs[k_num][1].plot(Xs, YsD, label=f"Displacements {select_type}", linewidth=LINEWIDTH)
                #axs[k_num][1].plot(XsLine, YsDLine, linewidth=1, color='red')
                
                axs[k_num][0].title.set_text(f"Comparisons of {select_type} for {gen_type} for k {k} of n")
                axs[k_num][1].title.set_text(f"Displacements of {select_type} for {gen_type} for k {k} of n")
                axs[k_num][0].legend()
                axs[k_num][1].legend()
                
        plot_path = os.path.join(PLOTS, f"{select_type}_{gen_type}.png")
        plt.tight_layout()
        plt.savefig(plot_path)
        plt.clf()
            
            
            
                    
                    
                    
                    
                    
                
            
            
if __name__ == "__main__":
    main()