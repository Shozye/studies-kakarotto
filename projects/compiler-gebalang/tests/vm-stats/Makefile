FLAGS = -W -pedantic -std=c++17 -O3

.PHONY = all clean cleanall

all: vm vm-cln

vm: lexer.o parser.o mw.o main.o
	$(CXX) $^ -o $@
	strip $@

vm-cln: lexer.o parser.o mw-cln.o main.o
	$(CXX) $^ -o $@ -l cln
	strip $@

%.o: %.cc
	$(CXX) $(FLAGS) -c $^

lexer.cc: lexer.l parser.hh
	flex -o $@ $<

parser.cc parser.hh: parser.y
	bison -Wall -d -o parser.cc $^

clean:
	rm -f *.o parser.cc parser.hh lexer.cc

cleanall: clean
	rm -f vm vm-cln
