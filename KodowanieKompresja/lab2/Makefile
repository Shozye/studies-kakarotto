all: programs/sandbox

programs/sandbox: src/sandbox.cpp programs/utils.o
	g++ -o programs/sandbox src/sandbox.cpp programs/utils.o

programs/utils.o: src/utils.cpp
	g++ -o programs/utils.o -c src/utils.cpp