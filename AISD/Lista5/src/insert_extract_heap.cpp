#include<iostream>
#include"max_heap.h"
#include"utils.h"

bool print = false;

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
    std::cout << "Generated: ";
    preety_print_list(nums, n);
    int heap[n];
    for(int i = 0; i < n; i++){
        insert(heap, i, nums[i]);
        if(print){
            std::cout << "Inserted " << nums[i] << std::endl;
            print_tree(heap, i);
        }
    }
    /*for(int i = n-1; i >= 0; i++){
        extract_max(heap, i);
        if(print){
            std::cout << "Deleted max " << std::endl;
            print_tree(heap, i);
        }
    }*/

    std::cout << get_amount_of_displacements() << " " << get_amount_of_comparisons() << std::endl;
}