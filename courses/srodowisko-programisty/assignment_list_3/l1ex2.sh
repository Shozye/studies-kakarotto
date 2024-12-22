# Mateusz Pełechaty 261737
# To do this task we need to 
# 1. Get all words from files
# 2. Put them into some structure to count them
# 3. print output
# By declaring with "-A" we are now declaring structure similar to
# dict in Python or unordered_map in c++
# Knowledge needed: https://linuxhint.com/associative_arrays_bash_examples/
declare -A freq
dir=$1
for file in $(./l1ex1.sh $dir ); do
    for word in $( cat $file ); do
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
    echo "$key: ${freq[$key]}"; 
done
