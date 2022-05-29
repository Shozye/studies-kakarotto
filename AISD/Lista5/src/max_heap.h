#pragma once

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
