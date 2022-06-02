import subprocess
import shutil
import os
from tqdm import tqdm
from itertools import product
from collections import defaultdict
import json
    

OUTPUT_FILE="data.json"
PROGRAMS_PATH = "../programs/"
GENERATE_PATH = PROGRAMS_PATH + "gen_rand"
TESTFILE_PATH = PROGRAMS_PATH + "insert_extract_heap"
MUL = 10000
START = 1 * MUL
END = 100 * MUL + 1
STEP = 10 * MUL
POSSIBLE_N = list(range(START, END, STEP))
AMOUNT_OF_TIMES_TO_REPEAT = 1

if not os.path.isfile(GENERATE_PATH) or not os.path.isfile(TESTFILE_PATH):
    raise Exception("Programs do not exist. \nUse make before running run.py")

data = defaultdict(list)

pbar = tqdm(POSSIBLE_N, "Parsing...")
for n in pbar:
    amount_displacements = 0
    amount_comparisons = 0
    for k in range(AMOUNT_OF_TIMES_TO_REPEAT):
        pbar.set_description(f"Parsing {TESTFILE_PATH.split('/')[-1]} for amount {n}/{END-1} ({k+1}/{AMOUNT_OF_TIMES_TO_REPEAT})")
        gen_ps = subprocess.Popen((GENERATE_PATH, str(n)), stdout=subprocess.PIPE)
        output = subprocess.check_output((TESTFILE_PATH), stdin=gen_ps.stdout)
        gen_ps.wait()
        output = output.decode('utf-8').strip().split(" ")
        amount_displacements += int(output[0])
        amount_comparisons += int(output[1])
    
    data["Xs"].append(n)
    data["displacements"].append(amount_displacements/AMOUNT_OF_TIMES_TO_REPEAT)
    data["comparisons"].append(amount_comparisons/AMOUNT_OF_TIMES_TO_REPEAT)
    
with open(OUTPUT_FILE, 'w+') as file:
    file.write(json.dumps(data, indent=4))