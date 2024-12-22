#include<iostream>
#include"utils.h"

int amount_of_comparisons = 0;
int amount_of_displacements = 0;
bool print = false;

void sort(int* nums, int n){
    int copy_nums[n];
    for(int i = 1; i < n; i++){
        copy(copy_nums, nums, n);
        int value_to_swap = nums[i];
        int j = i-1;
        while(value_to_swap < nums[j] && j >= 0){
            amount_of_comparisons += 1;
            amount_of_displacements++;
            nums[j+1] = nums[j];
            j--;
        }
        amount_of_displacements += 1;
        nums[j+1] = value_to_swap;
        if (print)
            preety_print_list_with_colours(nums, n, copy_nums);
    }
}

int main(int argc, char** argv){
    if (argc > 1) print=true;
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
    sort(nums, n);
    if (print){
        std::cout << "After sorting:" << std::endl;
        preety_print_list(nums, n);
    }
    check_if_list_sorted(nums, n);
    std::cout << amount_of_displacements << " " << amount_of_comparisons << std::endl;
}