all: programs/gen_asc programs/gen_desc programs/gen_rand programs/insert_sort programs/merge_sort programs/quick_sort programs/dual_pivot_quick_sort programs/hybrid_sort

programs/gen_asc: src/ascend_generator.cpp
	g++ -o programs/gen_asc src/ascend_generator.cpp

programs/gen_desc: src/descend_generator.cpp
	g++ -o programs/gen_desc src/descend_generator.cpp

programs/gen_rand: src/descend_generator.cpp
	g++ -o programs/gen_rand src/random_generator.cpp

programs/insert_sort: src/insert_sort.cpp
	g++ -o programs/insert_sort src/insert_sort.cpp

programs/merge_sort: src/merge_sort.cpp
	g++ -o programs/merge_sort src/merge_sort.cpp

programs/quick_sort: src/quick_sort.cpp
	g++ -o programs/quick_sort src/quick_sort.cpp

programs/dual_pivot_quick_sort: src/dual_pivot_quick_sort.cpp
	g++ -o programs/dual_pivot_quick_sort src/dual_pivot_quick_sort.cpp

programs/hybrid_sort: src/hybrid_sort.cpp
	g++ -o programs/hybrid_sort src/hybrid_sort.cpp