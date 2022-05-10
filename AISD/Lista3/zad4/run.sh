#!/bin/bash
set -m

rm -rf data
mkdir data

for n in {1000..100000..1000}
do
    mkdir "data/"$n
    let first=0
    let mid=$((n / 2))
    let last=$((n - 1))
    let not_in=-1
    let inside=-2
    for searched_element in $first $mid $last $not_in $inside
    do
        mkdir "data/"$n"/"$searched_element
        for m in {1..100}
        do
            ../programs/gen_asc $n 0 0 | ../programs/binary_search $searched_element > "data/"$n"/"$searched_element"/"$m
        done
    done
done 
