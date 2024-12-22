# Mateusz Pełechaty 261737
#!/bin/bash
# Example of working
# ./ex2.sh 15 21 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/
#

rev1=$1
rev2=$2
svn_dir=$3

#for tests
#rev1=15
#rev2=21
#svn_dir=https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/
#git log --stat
#git log --stat | grep -v '^commit ' | grep -v '^Author: ' | grep -v '^Date: '

# Extracts folder name
dir=$( echo $svn_dir | rev | cut -d'/' -f-2 | rev )
echo $dir

mkdir $dir
cd $dir
git init

for (( r=$rev1; r<=$rev2; r++ )) do
    svn export -q --force $svn_dir -r $r ./
    git add .
    git commit -m "$(svn log -r $r $svn_dir | tail -n +4 | head -n -2)"
    rm -rf *
done

cd ..