#!/bin/bash
rm -rf zad2_data
mkdir zad2_data

k=3

for i in {1..3}
do
    # Create a new file named k.txt (or clear it if it already exists)
    > zad2_data/k=_${k}_i=_${i}_.txt

    # Run the script 5 times
    for run in {1..5}
    do
        # Run the script and append the output to k.txt
        ./zad2.out --size ${k} --degree ${i} >> zad2_data/k=_${k}_i=_${i}_.txt
    done
done
echo $k done


for k in {4..10}
do
    for ((i=1; i<=k; i++))
    do
        # Create a new file named k.txt (or clear it if it already exists)
        > zad2_data/k=_${k}_i=_${i}_.txt

        # Run the script 5 times
        for run in {1..5}
        do
            # Run the script and append the output to k.txt
            ./zad2.out --size ${k} --degree ${i} >> zad2_data/k=_${k}_i=_${i}_.txt
        done
    done
    echo $k done
done
