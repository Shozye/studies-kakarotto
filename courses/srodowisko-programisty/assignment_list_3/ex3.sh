#/bin/bash
# Mateusz Pełechaty

# example: ./ex3.sh 15 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
# example: ./ex3.sh 18 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
rev="$1"
dir="$2"
declare -A freq

for file in $( ./svn_find_all_files.sh $rev $dir ); do
    for word in $( svn cat -r $rev "$dir""$file" | tr " " "\n" | sort | uniq ); do
        # checks if word is in freq map (chapter 5 in website)
        if [ $freq[$word]+_ ]; then 
            # https://stackoverflow.com/questions/8195583/how-can-i-increment-a-value-in-a-bash-script-array-by-1
            (( freq[$word]++ ))
        else 
            freq+=([$word]=1); 
        fi
    done
done

for key in "${!freq[@]}"; do 
    echo "$key :${freq[$key]}"; 
done
