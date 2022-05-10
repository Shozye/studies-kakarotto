#!/bin/bash

for n in 8 16 32
do
    rand=$RANDOM
    num=$((rand%n+1))
    # n = size
    # num is k-th smallet number to pick
    # 5 is partition divide size during select
    ../programs/gen_rand $n $num 5 | ../programs/select 
    ../programs/gen_rand $n $num 5 | ../programs/rand_select 
done