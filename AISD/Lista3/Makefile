all: programs/dual_pivot_quicksort programs/quicksort programs/quicksort_select programs/dual_pivot_quicksort_select programs/gen_asc programs/gen_desc programs/gen_rand programs/random_select programs/select programs/binary_search

programs/gen_asc: src/ascend_generator.cpp
	g++ -o programs/gen_asc src/ascend_generator.cpp

programs/gen_desc: src/descend_generator.cpp
	g++ -o programs/gen_desc src/descend_generator.cpp

programs/gen_rand: src/descend_generator.cpp
	g++ -o programs/gen_rand src/random_generator.cpp

programs/random_select: src/random_select.cpp
	g++ -o programs/random_select src/random_select.cpp

programs/binary_search: src/binary_search.cpp
	g++ -o programs/binary_search src/binary_search.cpp

programs/dual_pivot_quicksort_select: src/dual_pivot_quicksort_select.cpp
	g++ -o programs/dual_pivot_quicksort_select src/dual_pivot_quicksort_select.cpp

programs/quicksort_select: src/quicksort_select.cpp
	g++ -o programs/quicksort_select src/quicksort_select.cpp

programs/dual_pivot_quicksort: src/dual_pivot_quicksort.cpp
	g++ -o programs/dual_pivot_quicksort src/dual_pivot_quicksort.cpp

programs/quicksort: src/quicksort.cpp
	g++ -o programs/quicksort src/quicksort.cpp




programs/select: src/select.cpp
	g++ -o programs/select src/select.cpp