#!/bin/bash


test=B


lex -o ex.c ex.l
gcc ex.c -o ex.out
cat ./tests/test$test.txt | ./ex.out > tests/last_run.txt
rm ex.c ex.out

echo "Check diff? (y/n)"

read answer

if [ $answer = y ]; then
    diff ./tests/last_run.txt ./tests/ans$test.txt
fi
