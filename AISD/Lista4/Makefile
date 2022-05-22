p=programs/
s=src/

all: directories ${p}rand_gen ${p}BST_test

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

${p}utils.o: ${s}utils.cpp
	g++ -c -o ${p}utils.o ${s}utils.cpp 


