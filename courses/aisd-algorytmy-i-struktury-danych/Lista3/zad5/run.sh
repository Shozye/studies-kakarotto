#!/bin/bash
set -m

rm -rf data
mkdir data

for n in {100..10000..100}
do
    for algo_name in "dual_pivot_quicksort" "dual_pivot_quicksort_select" "quicksort" "quicksort_select"
    do  

        algo="../programs/"$algo_name
        for gen_type in "gen_rand" "gen_asc" "gen_desc"
        do
            gen="../programs/"$gen_type
            for m in {1..10..1}
            do
                $gen $n 0 0 | $algo > "data/"$algo_name"_"$gen_type"_"$n"_"$m
            done
        done
    done
    echo $n
done