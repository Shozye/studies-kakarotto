#!/bin/bash

lexe=./ex.l
cexe=./ex.c
exe=./ex.out

test_dir=./tests
test=$test_dir"/test.cpp"

parsed=$test_dir"/parsed_test.cpp"

lex -o $cexe $lexe
gcc $cexe -o $exe
cat $test | ./ex.out > $parsed
rm $cexe $exe
