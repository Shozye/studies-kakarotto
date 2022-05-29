p=programs/
s=src/

all: directories generators previous_sorts heap

clean:
	rm programs/*

directories:
	mkdir -p ${p}

generators: ${p}gen_asc ${p}gen_desc ${p}gen_rand

previous_sorts: ${p}insert_sort ${p}merge_sort ${p}quick_sort ${p}dual_pivot_quick_sort ${p}hybrid_sort

heap: ${p}max_heap_test


${p}max_heap_test: ${s}max_heap_test.cpp ${p}max_heap.o ${p}utils.o
	g++ -o ${p}max_heap_test ${s}max_heap_test.cpp ${p}max_heap.o ${p}utils.o

${p}max_heap.o: ${s}max_heap.cpp
	g++ -c -o ${p}max_heap.o ${s}max_heap.cpp

${p}utils.o: ${s}utils.cpp
	g++ -c -o ${p}utils.o ${s}utils.cpp 

${p}gen_asc: ${s}ascend_generator.cpp ${p}utils.o
	g++ -o ${p}gen_asc ${s}ascend_generator.cpp ${p}utils.o

${p}gen_desc: ${s}descend_generator.cpp ${p}utils.o
	g++ -o ${p}gen_desc ${s}descend_generator.cpp ${p}utils.o

${p}gen_rand: ${s}descend_generator.cpp ${p}utils.o
	g++ -o ${p}gen_rand ${s}random_generator.cpp ${p}utils.o

${p}insert_sort: ${s}insert_sort.cpp ${p}utils.o
	g++ -o ${p}insert_sort ${s}insert_sort.cpp ${p}utils.o

${p}merge_sort: ${s}merge_sort.cpp ${p}utils.o
	g++ -o ${p}merge_sort ${s}merge_sort.cpp ${p}utils.o

${p}quick_sort: ${s}quick_sort.cpp ${p}utils.o
	g++ -o ${p}quick_sort ${s}quick_sort.cpp ${p}utils.o

${p}dual_pivot_quick_sort: ${s}dual_pivot_quick_sort.cpp ${p}utils.o
	g++ -o ${p}dual_pivot_quick_sort ${s}dual_pivot_quick_sort.cpp ${p}utils.o

${p}hybrid_sort: ${s}hybrid_sort.cpp ${p}utils.o
	g++ -o ${p}hybrid_sort ${s}hybrid_sort.cpp ${p}utils.o
