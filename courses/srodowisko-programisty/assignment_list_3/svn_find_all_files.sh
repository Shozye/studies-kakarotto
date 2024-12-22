#!/bin/bash
# Mateusz Pelechaty 261737
# example: ./svn_find_all_files.sh 15 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
# example: ./svn_find_all_files.sh 18 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
rev="$1"
dir="$2"

# loop over the files in this directory recursively
for file in $( svn ls -r $rev $dir -R ); do
    # if it is not a directory — print out its full path
    if [ "${file: -1}" != "/" ]; then
        echo $file
    fi
done
