import subprocess
import shutil
import os
from numpy import insert
from tqdm import tqdm
from itertools import product
from collections import defaultdict
import json
    

OUTPUT_FILE="data.json"
PROGRAMS_PATH = "../programs/"
GENERATE_PATH = PROGRAMS_PATH + "gen_rand"
SORT_TYPES = ["insert_sort", "merge_sort", "dual_pivot_quick_sort", "quick_sort", "hybrid_sort" ,"max_heap_test"]
TESTFILES_PATH = [PROGRAMS_PATH + sort_type for sort_type in SORT_TYPES]
MUL = 100
START = 1 * MUL
END = 10 * MUL + 1
STEP = 1 * MUL
POSSIBLE_N = list(range(START, END, STEP))
AMOUNT_OF_TIMES_TO_REPEAT = 100

if not os.path.isfile(GENERATE_PATH) or not all([os.path.isfile(x) for x in TESTFILES_PATH]):
    raise Exception("Programs do not exist. \nUse make before running run.py")

data = dict()

pbar = tqdm(product(TESTFILES_PATH, POSSIBLE_N), "Parsing...")
for testfile_path, n in pbar:
    
    amount_displacements = 0
    amount_comparisons = 0
    for k in range(AMOUNT_OF_TIMES_TO_REPEAT):
        pbar.set_description(f"Parsing {testfile_path.split('/')[-1]} for amount {n}/{END-1} ({k+1}/{AMOUNT_OF_TIMES_TO_REPEAT})")
        gen_ps = subprocess.Popen((GENERATE_PATH, str(n)), stdout=subprocess.PIPE)
        output = subprocess.check_output((testfile_path), stdin=gen_ps.stdout)
        gen_ps.wait()
        output = output.decode('utf-8').strip().split(" ")
        amount_displacements += int(output[0])
        amount_comparisons += int(output[1])
    
    sort_name = testfile_path.split("/")[-1]
    if data.get(sort_name) == None:
        data[sort_name] = defaultdict(list)
    data[sort_name]["Xs"].append(n)
    data[sort_name]["displacements"].append(amount_displacements/AMOUNT_OF_TIMES_TO_REPEAT)
    data[sort_name]["comparisons"].append(amount_comparisons/AMOUNT_OF_TIMES_TO_REPEAT)
    
with open(OUTPUT_FILE, 'w+') as file:
    file.write(json.dumps(data, indent=4))