p=../programs/

echo "Two arrays generated by gen_asc 10"
${p}gen_asc 20 | ${p}longest_common_substring PRINT
echo "Two arrays generated by gen_rand 10"
${p}gen_rand 20 | ${p}longest_common_substring PRINT