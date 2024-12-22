# Mateusz Pełechaty 261737

dir=$1
all_words=$( ./ex3.sh $dir )
for word in $all_words; do
    # i am doing here what's known as SUBSTRING EXTRACTION
    # https://tldp.org/LDP/abs/html/string-manipulation.html
    # because $word is either word or ":amount"
    if [ ${word:0:1} != ":" ]; then
        # r is recursive over directory, n is print line, E is extended regex
        # we are searching for at least two times word in the line so grep
        x=$( grep -rnE "(^| )"$word"( | .* )"$word"( |$)" $dir );
        # if x has found any lines then we want to print it
        if [ "$x" != "" ]; then
            echo $word
            echo $x;
        fi
    fi
done;
