all: programs/sandbox programs/encode

programs/sandbox: src/sandbox.cpp programs/utils.o
	g++ -o programs/sandbox src/sandbox.cpp programs/utils.o

programs/encode: src/encode.cpp programs/utils.o
	g++ -o programs/encode src/encode.cpp programs/utils.o

programs/decode: src/decode.cpp programs/utils.o
	g++ -o programs/decode src/decode.cpp programs/utils.o

programs/utils.o: src/utils.cpp
	g++ -o programs/utils.o -c src/utils.cpp

