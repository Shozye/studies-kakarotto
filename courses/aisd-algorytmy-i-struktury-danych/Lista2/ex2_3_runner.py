from operator import sub
import subprocess
import sys
import json

def main():
    data = dict()
    for sort_type in ["insert_sort", "merge_sort", "quick_sort", "dual_pivot_quick_sort", "hybrid_sort"]:
        data[sort_type] = dict()
        print(f"Starting {sort_type}")
        for gen_type in ["gen_asc", "gen_desc", "gen_rand"]:
            print(f"Starting {gen_type}")
            data[sort_type][gen_type] = dict()
            for n in range(100, 1001, 50):
                data[sort_type][gen_type][n] = dict()
                for k in [1, 10, 100]:
                    displacements = []
                    comparisons = []
                    for _ in range(k):       
                        result = subprocess.Popen([f"programs/{gen_type}", f"{n}"], stdout=subprocess.PIPE)
                        sort_result = subprocess.check_output([f"programs/{sort_type}"], stdin=result.stdout)
                        displacement, comparison = list(map(int, sort_result.decode("utf-8").split(":")))
                        displacements.append(displacement)
                        comparisons.append(comparison)
                    data[sort_type][gen_type][n][k] = {"avg_displacements": sum(displacements)/k,
                                                       "avg_comparisons": sum(comparisons)/k }
    with open("data_to_visualize.json", 'w+') as file:
        file.write(json.dumps(data))


if __name__ == "__main__":
    main()