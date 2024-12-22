p=programs/
s=src/

all: directories ${p}rand_gen ${p}BST_test ${p}Red_black_tree ${p}SplayTree_test

clean:
	rm programs/*

directories:
	mkdir -p ${p}

${p}rand_gen: ${p}rand_gen.o ${p}utils.o
	g++ -o ${p}rand_gen ${p}rand_gen.o ${p}utils.o

${p}rand_gen.o: ${s}rand_gen.cpp
	g++ -c -o ${p}rand_gen.o ${s}rand_gen.cpp 

${p}BST_test: ${p}BST_test.o ${p}BST.o ${p}utils.o
	g++ -o ${p}BST_test ${p}BST_test.o ${p}BST.o ${p}utils.o

${p}BST_test.o: ${s}BST_test.cpp 
	g++ -c -o ${p}BST_test.o ${s}BST_test.cpp 

${p}BST.o: ${s}BST.cpp 
	g++ -c -o ${p}BST.o ${s}BST.cpp

${p}SplayTree_test: ${p}SplayTree_test.o ${p}SplayTree.o ${p}utils.o
	g++ -o ${p}SplayTree_test ${p}SplayTree_test.o ${p}SplayTree.o ${p}utils.o

${p}SplayTree_test.o: ${s}SplayTree_test.cpp 
	g++ -c -o ${p}SplayTree_test.o ${s}SplayTree_test.cpp 

${p}SplayTree.o: ${s}SplayTree.cpp 
	g++ -c -o ${p}SplayTree.o ${s}SplayTree.cpp

${p}Red_black_tree: ${s}Red_black_tree.cpp ${p}utils.o
	g++ -o ${p}Red_black_tree ${s}Red_black_tree.cpp ${p}utils.o

${p}utils.o: ${s}utils.cpp
	g++ -c -o ${p}utils.o ${s}utils.cpp 


