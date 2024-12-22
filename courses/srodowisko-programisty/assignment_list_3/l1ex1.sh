#/bin/bash
# Mateusz Pełechaty 261737
dir=$1
find $dir -type f -not -path "*/.svn/*"
