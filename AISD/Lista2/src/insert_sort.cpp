#include<iostream>
#include"utils.cpp"

int amount_of_comparisons = 0;
int amount_of_displacements = 0;
void sort(int* nums, int n){
    int copy_nums[n];
    for(int i = 1; i < n; i++){
        copy(copy_nums, nums, n);
        amount_of_comparisons++; // Porownywanie czy i < n
        int value_to_swap = nums[i];
        amount_of_displacements++; // Dostep tez mozna liczyc
        int j = i-1;
        while(value_to_swap < nums[j] && j >= 0){
            amount_of_comparisons += 2; // dwa warunki w while
            nums[j+1] = nums[j];
            amount_of_displacements++; // linijka wyzej
            j--;
        }
        nums[j+1] = value_to_swap;
        amount_of_displacements += 1; // linijka wyzej
        if (n < 50)
            preety_print_list_with_colours(nums, n, copy_nums);
    }
}

int main(){
    int n;
    std::cin >> n;
    int nums[n];

    for(int i = 0; i < n; i++){
        std::cin >> nums[i];
    }
    if(n < 50){
        std::cout << "Before sorting:" << std::endl;
        preety_print_list(nums,n);
        std::cout << "During sorting:" << std::endl;
    }
    sort(nums, n);
    if (n < 50){
        std::cout << "After sorting:" << std::endl;
        preety_print_list(nums, n);
    }
    check_if_list_sorted(nums, n);
    std::cout << amount_of_displacements << ":" << amount_of_comparisons << std::endl;
}