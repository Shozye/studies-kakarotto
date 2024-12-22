#!/bin/bash
rm -rf zad1_data
mkdir zad1_data
# Loop from 1 to 16
for k in {1..16}
do
    # Create a new file named k.txt (or clear it if it already exists)
    > zad1_data/${k}.txt

    # Run the script 5 times
    for i in {1..2}
    do
        # Run the script and append the output to k.txt
        ./zad1.out --size ${k} >> zad1_data/${k}.txt
    done
done
