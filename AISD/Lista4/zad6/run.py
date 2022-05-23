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
GENERATE_PATH = PROGRAMS_PATH + "rand_gen"
TESTFILE_PATH = PROGRAMS_PATH + "SplayTree"
MUL = 10000
START = 1 * MUL
END = 10 * MUL + 1
STEP = 1 * MUL
AMOUNT_OF_TIMES_TO_REPEAT = 20

if not (os.path.isfile(GENERATE_PATH) or os.path.isfile(TESTFILE_PATH)):
    raise Exception("Programs do not exist. \nUse make before running run.py")

INSERT_TYPES = ["ASCENDING", "RANDOM"]
data = dict()
for insert_type in INSERT_TYPES:
    data[insert_type] = dict()
    for n in range(START, END, STEP):
        data[insert_type][n] = defaultdict(int)

pbar = tqdm(product(INSERT_TYPES, range(START, END, STEP), range(AMOUNT_OF_TIMES_TO_REPEAT)), "Parsing...")
for insert_type, n, i in pbar:
    pbar.set_description(f"Parsing {insert_type} for amount {n}.{i}")
    gen_ps = subprocess.Popen((GENERATE_PATH, str(n), 'DISTINCT'), stdout=subprocess.PIPE)
    output = subprocess.check_output((TESTFILE_PATH, insert_type, 'WHATEVER'), stdin=gen_ps.stdout)
    gen_ps.wait()
    output = output.decode('utf-8').strip().split(" ")
    mean_comp, mean_disp, mean_h, max_comp, max_disp, max_h = list(map(float, output))
    data[insert_type][n]['mean_comp'] += mean_comp
    data[insert_type][n]['mean_disp'] += mean_disp
    data[insert_type][n]['mean_h'] += mean_h
    data[insert_type][n]['max_comp'] += max_comp
    data[insert_type][n]['max_disp'] += max_disp
    data[insert_type][n]['max_h'] += max_h

for insert_type, n in product(INSERT_TYPES, range(START, END, STEP)):
    data[insert_type][n]['mean_comp'] /= AMOUNT_OF_TIMES_TO_REPEAT
    data[insert_type][n]['mean_disp'] /= AMOUNT_OF_TIMES_TO_REPEAT
    data[insert_type][n]['mean_h'] /= AMOUNT_OF_TIMES_TO_REPEAT
    data[insert_type][n]['max_comp'] /= AMOUNT_OF_TIMES_TO_REPEAT
    data[insert_type][n]['max_disp'] /= AMOUNT_OF_TIMES_TO_REPEAT
    data[insert_type][n]['max_h'] /= AMOUNT_OF_TIMES_TO_REPEAT
    
with open(OUTPUT_FILE, 'w+') as file:
    file.write(json.dumps(data, indent=4))