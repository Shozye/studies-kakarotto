#!/bin/bash

lexe=./ex.l
cexe=./ex.c
exe=./ex.out

test_dir=./tests
test_start=1
test_end=13
test_input=in.txt
test_output=actual.txt


lex -o $cexe $lexe
gcc $cexe -o $exe

for (( i=$test_start; i<=$test_end; i+=1 )); do
    cat $test_dir/$i/$test_input | $exe > $test_dir/$i/$test_output
done;

rm $cexe $exe
