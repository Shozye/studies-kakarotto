#include<iostream>
#include"utils.cpp"

int amount_of_displacements = 0;
int amount_of_comparisons = 0;

void insert_sort(int* nums, int n, int start, int end){
    int copy_nums[n];
    for(int i = start+1; i <= end; i++){
        copy(copy_nums, nums, n);
        amount_of_comparisons++; // Porownywanie czy i < n
        int value_to_swap = nums[i];
        amount_of_displacements++; // Dostep tez mozna liczyc
        int j = i-1;
        while(value_to_swap < nums[j] && j >= start){
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

int Partition(int* nums, int low, int high){
    int pivot = nums[low];
    amount_of_displacements++; // slyszalem ze takie cos tez zapisujemy
    int leftwall = low+1;
    int temp; // only to swap

    for(int i = low + 1; i <= high; i++){
        amount_of_comparisons++; // warunek fora
        if (nums[i] < pivot) {
            amount_of_comparisons++; // 
            amount_of_displacements++; // jednoczesnie dobieramy wartosc z tablicy i porownujemy
            temp = nums[i];
            nums[i] = nums[leftwall];
            nums[leftwall] = temp;
            leftwall++;
            amount_of_displacements++; // swap to 3 zmiany listy
        }
    }
    temp = pivot;
    nums[low] = nums[leftwall-1];
    nums[leftwall-1] = pivot;
    amount_of_displacements+=2; // ekhem ekhem

    return leftwall-1;
}

void quick_sort(int* nums, int n, int low, int high){
    if (low >= high){
        amount_of_comparisons++; // w ifie
        return;
    }
    amount_of_comparisons++; // w ifie
    int copy_nums[n];
    copy(copy_nums, nums, n);
    if (high - low >= 15){
        int pivot_location = Partition(nums, low, high);
        if (n < 50)
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