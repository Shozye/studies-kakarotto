
EXE="./run.out"
DATASET_DIR="./ch9-1.1/inputs"
ALGORITHM=dial
EXTENSION="ss"


type=USA-road-t
algorithms=("dijkstra" "dial")
cities=("BAY" "NY" "NW")


for algorithm in "${algorithms[@]}"
do
    for city in "${cities[@]}"
    do
        BASE=$type.$city
        DD_FILE="$BASE.gr"
        echo "Running tests with file: $DD_FILE"


        TASK_FILE="$BASE.ss"
        OUT_FILE="$BASE.$ALGORITHM.oss"

        $EXE $ALGORITHM -d "$DATASET_DIR/$type/$DD_FILE" -ss "$DATASET_DIR/$type/$TASK_FILE" -oss "$DATASET_DIR/$type/$OUT_FILE"

        TASK_FILE="$BASE.p2p"
        OUT_FILE="$BASE.$ALGORITHM.op2p"

        $EXE $ALGORITHM -d "$DATASET_DIR/$type/$DD_FILE" -p2p "$DATASET_DIR/$type/$TASK_FILE" -op2p "$DATASET_DIR/$type/$OUT_FILE"


    done
done
