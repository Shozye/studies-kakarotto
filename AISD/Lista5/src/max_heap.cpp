#include "max_heap.h"
#include "utils.h"
#include<iostream>
#include <stdexcept>
#include<vector>

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

void heap_increase_key(int* tab, int i, int key){
    if(key < tab[i]){
        throw std::invalid_argument("New key is smaller than MIN_INT");
    }
    tab[i] = key;
    while(i > 0 && tab[parent(i)] < tab[i]){
        swap(&tab[i], &tab[parent(i)]);
        i=parent(i);
    }
}

void print_tree(int* tab, int length, int index, std::vector<int> path){
    int l = left(index);
    int r = right(index);

    if (l < length && l >= 0){
        std::vector<int> pathl = path;
        pathl.push_back(1);
        print_tree(tab, length, l, pathl);
    }
    int prev = -1;
    for(int i = path.size()-1; i >= 0; i--){
        if(prev == path[i]) std::cout << " ";
        else if (prev == (-1)*path[i]) std::cout << "|";
    }
    std::cout << "-[" << tab[index] << "]" << std::endl;
    if (r < length && r >= 0){
        std::vector<int> pathr = path;
        pathr.push_back(-1);
        print_tree(tab, length, r, pathr);
    }
}

void print_tree(int* tab, int length){
    std::vector<int> path;
    print_tree(tab, length, 0, path);
}

void insert(int* tab, int length, int key){
    tab[length] = INT32_MIN;
    heap_increase_key(tab, length, key);
}
int extract_max(int* tab, int length){
    if(length < 0)
        throw std::invalid_argument("Heap empty");
    int max = tab[0];
    tab[0] = tab[length-1];
    max_heapify(tab, length-1, length-1, 0);
    return max;
}