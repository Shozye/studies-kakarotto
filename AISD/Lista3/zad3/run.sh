#!/bin/bash
set -m

rm -rf data
mkdir data
for select_type in "random_select" "select"
do
    mkdir "data/"$select_type
    for gen_type in "gen_asc" "gen_desc" "gen_rand"
    do
        mkdir "data/"$select_type"/"$gen_type
        for k in 3 5 7 9
        do
            mkdir "data/"$select_type"/"$gen_type"/"$k
            mkdir "data/"$select_type"/"$gen_type"/"$k"/first"
            mkdir "data/"$select_type"/"$gen_type"/"$k"/quarter"
            mkdir "data/"$select_type"/"$gen_type"/"$k"/half"
            for n in {100..10000..100}
            do
                for m in {1..100}
                do
                    let "k1 = 1"
                    let "k2 = n/4"
                    let "k3 = n/2" 

                    "../programs/"$gen_type $n $k1 $k | "../programs/"$select_type > "data/"$select_type"/"$gen_type"/"$k"/first/n_"$n"_m_"$m".txt"
                    "../programs/"$gen_type $n $k2 $k | "../programs/"$select_type > "data/"$select_type"/"$gen_type"/"$k"/quarter/n_"$n"_m_"$m".txt"
                    "../programs/"$gen_type $n $k3 $k | "../programs/"$select_type > "data/"$select_type"/"$gen_type"/"$k"/half/n_"$n"_m_"$m".txt"
                done
            done
            echo "done "$select_type"_"$gen_type"_"$k
        done
        echo "done "$select_type"_"$gen_type
    done
    echo "done "$select_type
done
echo "done"
