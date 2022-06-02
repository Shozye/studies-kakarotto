#include<iostream>
#include"utils.h"

int amount_of_comparisons = 0;
int amount_of_displacements = 0;
bool print = false;

void merge(int* nums, int left, int right){
    int save_begin = left;
    int LS = left;
    int LE = left + ( right - left ) / 2;
    int RS = LE + 1;
    int RE = right;
    int size = right - left + 1;
    int temp[size];
    int index = 0;

    while (LS <= LE && RS <= RE){
        amount_of_comparisons += 1;
        amount_of_displacements += 1;
        if (nums[LS] <= nums[RS]){
            temp[index] = nums[LS];
            LS++;
        }
        else {
            temp[index] = nums[RS];
            RS++;
        }
        index++;
    }

    while (LS <= LE){
        temp[index] = nums[LS];
        amount_of_displacements++; // linijka wyzej
        LS++;
        index++;
    }
    while (RS <= RE){
        temp[index] = nums[RS];
        amount_of_displacements++; // linijka wyzej
        RS++;
        index++;
    }
    for(int i = 0; i < size; i++){
        nums[save_begin + i] = temp[i];
        amount_of_displacements++;
    }
}

void mergesort(int* nums, int n, int left, int right){
    if (left >= right)
        return;
    int middle = left + ( right - left ) / 2;
    int copy_nums[n];
    copy(copy_nums, nums, n);
    mergesort(nums, n, left, middle);
    mergesort(nums, n, middle+1, right);
    merge(nums, left, right);
    if (print)
        preety_print_list_with_colours(nums, n, copy_nums);
}

void sort(int* nums, int n){
    mergesort(nums, n, 0, n-1);
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