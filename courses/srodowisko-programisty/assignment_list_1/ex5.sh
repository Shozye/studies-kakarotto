dir="./a"
all_files=$( ./ex1.sh $dir )
#For every file
for file in $all_files; do
    # We are printing and translating words from content

    ( cat $file | tr "a" "A" ) > temp_file.txt;
    mv temp_file.txt $file
    # we re-write content to file
done
