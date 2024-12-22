FLAGS = -std=c++11 -lfl
.PHONY = all clean cleanall

all: calc

calc: calc.y calc.l
	bison -d -o build/calc.tab.cpp calc.y
	g++ -c build/calc.tab.cpp -o build/calc.tab.o
	flex -obuild/calcl.cpp calc.l
	g++ $(FLAGS) -c build/calcl.cpp -o build/calcl.o
	g++ -c utils.cpp -o build/utils.o
	g++ -o calc build/calcl.o build/calc.tab.o build/utils.o
	rm -f build/*.cpp build/*.hpp build/*.o
	
clean:
	rm -f build/*.cpp build/*.hpp build/*.o

cleanall: clean
	rm -f calc
