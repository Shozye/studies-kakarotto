
EXE="./run.out"
DATASET_DIR="./ch9-1.1/inputs"
ALGORITHM=dial
EXTENSION="ss"
INT_MIN=16
INT_MAX=18

types=("Long-n" "Square-n")

for type in "${types[@]}"
do
  for (( i=INT_MIN; i<=INT_MAX; i++ ))
  do
    DD_FILE="$type.$i.0.gr"
    echo "Running tests with file: $DD_FILE"

    if [ "$EXTENSION" = "ss" ]; then
      SS_FILE="$type.$i.0.ss"
      OUT_FILE="$type.$i.0.$ALGORITHM.oss"

      $EXE $ALGORITHM -d "$DATASET_DIR/$type/$DD_FILE" -ss "$DATASET_DIR/$type/$SS_FILE" -oss "$DATASET_DIR/$type/$OUT_FILE"
    fi
  done
done