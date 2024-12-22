
EXE="./run.out"
DATASET_DIR="./ch9-1.1/inputs"
ALGORITHM=dial
EXTENSION="ss"


INT_MIN=0
INT_MAX=15

types=("Random4-C" "Long-C" "Square-C")
algorithms=("dijkstra" "dial")

for algorithm in "${algorithms[@]}"
do
    for type in "${types[@]}"
    do
        for (( i=INT_MIN; i<=INT_MAX; i++ ))
        do
            DD_FILE="$type.$i.0.gr"
            echo "Running tests with file: $DD_FILE"

            if [ "$EXTENSION" = "ss" ]; then
                TASK_FILE="$type.$i.0.ss"
                OUT_FILE="$type.$i.0.$ALGORITHM.oss"

                $EXE $ALGORITHM -d "$DATASET_DIR/$type/$DD_FILE" -ss "$DATASET_DIR/$type/$TASK_FILE" -oss "$DATASET_DIR/$type/$OUT_FILE"
            else
                TASK_FILE="$type.$i.0.p2p"
                OUT_FILE="$type.$i.0.$ALGORITHM.op2p"

                $EXE $ALGORITHM -d "$DATASET_DIR/$type/$DD_FILE" -p2p "$DATASET_DIR/$type/$TASK_FILE" -op2p "$DATASET_DIR/$type/$OUT_FILE"
            fi
        done
    done
done
