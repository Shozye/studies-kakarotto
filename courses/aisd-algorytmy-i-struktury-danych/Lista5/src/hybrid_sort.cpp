#include<iostream>
#include"utils.h"

int amount_of_comparisons = 0;
int amount_of_displacements = 0;
bool print = false;

void swap(int* a, int* b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
    amount_of_displacements += 3;
}

void insert_sort(int* nums, int n, int start, int end){
    int copy_nums[n];
    for(int i = start+1; i <= end; i++){
        copy(copy_nums, nums, n);
        int value_to_swap = nums[i];
        int j = i-1;
        amount_of_comparisons += 1;
        while(value_to_swap < nums[j] && j >= start){
            amount_of_comparisons++;
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

int Partition(int* nums, int low, int high){
    int pivot = nums[low];
    int leftwall = low+1;
    for(int i = low + 1; i <= high; i++){
        amount_of_comparisons++; 
        if (nums[i] < pivot) {
            amount_of_displacements+=3;
            swap(&nums[i], &nums[leftwall]);
            leftwall++;
            amount_of_displacements++; // swap to 3 zmiany listy
        }
    }
    swap(&nums[low], &nums[leftwall-1]);
    return leftwall-1;
}

void quick_sort(int* nums, int n, int low, int high){
    if (low >= high){
        return;
    }
    int copy_nums[n];
    copy(copy_nums, nums, n);
    if (high - low >= 15){
        int pivot_location = Partition(nums, low, high);
        if (print)
            preety_print_list_with_colours(nums, n, copy_nums);
        quick_sort(nums, n, low, pivot_location);
        quick_sort(nums, n, pivot_location+1, high);
    }
    else{
        insert_sort(nums, n, low, high);
    }
}

void sort(int* nums, int n){
    quick_sort(nums, n, 0, n-1);
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