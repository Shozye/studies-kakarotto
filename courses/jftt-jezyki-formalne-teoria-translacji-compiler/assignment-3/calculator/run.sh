#!/bin/bash

exe=./calc

test_dir=./tests
test_start=1
test_end=21
test_input=in.txt
test_output=actual.txt
test_expected=expected.txt

for (( i=$test_start; i<=$test_end; i+=1 )); do
    cat $test_dir/$i/$test_input | $exe > $test_dir/$i/$test_output

    echo TEST $i
    cat $test_dir/$i/$test_input
    echo EXPECTED
    cat $test_dir/$i/$test_expected
    echo ACTUAL
    cat $test_dir/$i/$test_output
done;

