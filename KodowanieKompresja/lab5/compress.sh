p=pictures/
c=pictures/example

for k in {0..11..1}
do
  for photo_type in {0..3..1}
  do
  python3 lgbtq+.py ${p}example"${photo_type}".tga ${c}"${photo_type}"/example"${photo_type}"_"${k}".tga "${k}"
  done
done