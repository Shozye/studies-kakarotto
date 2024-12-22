#/bin/bash
# Mateusz Pełechaty

# example: ./ex2_checkout.sh 15 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
# example: ./ex2_checkout.sh 18 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
rev="$1"
dir="$2"

svn co -r $rev $dir > /dev/null

./l1ex2.sh a

rm -rf a
