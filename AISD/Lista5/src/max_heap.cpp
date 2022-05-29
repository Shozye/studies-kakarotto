#include "max_heap.h"
#include "utils.h"
#include<iostream>

int amount_of_comparisons = 0;
int amount_of_displacements = 0;
bool print_flag = false;


int get_amount_of_displacements(){return amount_of_displacements;}
int get_amount_of_comparisons(){return amount_of_comparisons;}

void set_print(){
    print_flag = true;
}

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
    amount_of_displacements += 3;
}
 

int left(int i){
    return 2*i+1;
}
int parent(int i){
    return (i-1)/2;
}
int right(int i){
    return 2*i + 2;
}
void max_heapify(int* A, int length, int heap_size, int i){
    int largest, l, r;
    l = left(i);
    r = right(i);
    amount_of_comparisons += 1;
    if (l < heap_size && A[l] > A[i])
        largest = l;
    else
        largest = i;
    amount_of_comparisons += 1;
    if (r < heap_size && A[r] > A[largest])
        largest = r;
    if (largest != i){
        swap(&A[largest], &A[i]);
        max_heapify(A, length, heap_size, largest);
    }
}

void build_max_heap(int* A, int length, int heap_size){
    for(int i = (heap_size-1)/2; i>=0; i--){
        max_heapify(A, length, heap_size, i);
    }
}

void heapsort(int* A, int length){
    int heap_size = length;
    build_max_heap(A, length, heap_size);
    for(int i = heap_size - 1; i > 0; i--){
        swap(&A[0], &A[i]);
        heap_size -= 1;
        max_heapify(A, length, heap_size, 0);
        if (print_flag){
            preety_print_list(A, length);
        }
    }
}
