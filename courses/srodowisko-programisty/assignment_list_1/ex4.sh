# Mateusz Pełechaty 261737
dir=$1
all_words=$( ./ex3.sh $dir )
for word in $all_words; do
    # i am doing here what's known as SUBSTRING EXTRACTION
    # https://tldp.org/LDP/abs/html/string-manipulation.html
    # i am doing this because words in ex3.sh also come 
    # with their amount prepended with :
    if [ ${word:0:1} != ":" ]; then
        echo $word
        # r is recursive over directory, n is print line, E is extended regex
        grep -rnE '(^| )'$word'($| )' $dir
        
    fi
done;
