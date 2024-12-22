#pragma once
#include<vector>

int get_amount_of_displacements();
int get_amount_of_comparisons();
void set_print();
void heapsort(int* tab, int length);
void swap(int*, int*);
int left(int x);
int parent(int x);
int right(int x);
void max_heapify(int* tab, int length, int heap_size, int i);
void build_max_heap(int* tab, int length, int heap_size);
void insert(int* tab, int length, int x);
int extract_max(int* tab, int length);
void print_tree(int* tab, int length, int index, std::vector<int> path);
void print_tree(int* tab, int length);
