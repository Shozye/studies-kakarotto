from operator import ge


with open("ex1_tests.sh", 'w+') as file:
    file.write("#!/bin/bash\n\n")
    for sort_type in ["insert_sort", "merge_sort", "quick_sort"]:
        for generator_type in ["gen_rand", "gen_desc", "gen_asc"]:
            for n in [8,16,32]:
                file.write(f"echo '{generator_type} for n = {n}. sort = {sort_type}'\n")
                file.write(f"programs/{generator_type} {n} | programs/{sort_type}\n")

with open("ex3_tests.sh", 'w+') as file:
    file.write("#!/bin/bash\n\n")
    sort_type = "dual_pivot_quick_sort"
    for generator_type in ["gen_rand", "gen_desc", "gen_asc"]:
        for n in [8,16,32]:
            file.write(f"echo '{generator_type} for n = {n}. sort = {sort_type}'\n")
            file.write(f"programs/{generator_type} {n} | programs/{sort_type}\n")

with open("ex4_tests.sh", "w+") as file:
    file.write("#!/bin/bash\n\n")
    sort_type = "hybrid_sort"
    for generator_type in ["gen_rand", "gen_desc", "gen_asc"]:
        for n in [8,16,32]:
            file.write(f"echo '{generator_type} for n = {n}. sort = {sort_type}'\n")
            file.write(f"programs/{generator_type} {n} | programs/{sort_type}\n")