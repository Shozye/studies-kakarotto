#include<iostream>
#include"max_heap.h"
#include"utils.h"

bool print = false;

void tests(){
    int length, heap_size;
    int A[] = {4,1,3,2,16,9,10,14,8,7};
    length = 10;
    heap_size = 10;
    preety_print_list(A, length);
    build_max_heap(A, length, heap_size);
    preety_print_list(A, length);

    int B[] = {16, 4, 10, 14, 7, 9, 3, 2, 8, 1};
    preety_print_list(B, length);
    max_heapify(B, length, heap_size, 1);
    preety_print_list(B, length);
}

int main(int argc, char** argv){
    if (argc > 1){
        print=true;
        set_print();
    }

    int n;
    std::cin >> n;
    int nums[n];

    for(int i = 0; i < n; i++){
        std::cin >> nums[i];
    }
    if(print){
        std::cout << "Before sorting:" << std::endl;
        preety_print_list(nums,n);
        std::cout << "During sorting:" << std::endl;
    }
    heapsort(nums, n);
    if (print){
        std::cout << "After sorting:" << std::endl;
        preety_print_list(nums, n);
    }
    check_if_list_sorted(nums, n);

    std::cout << get_amount_of_displacements() << " " << get_amount_of_comparisons() << std::endl;
}