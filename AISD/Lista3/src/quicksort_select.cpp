#include<iostream>
#include"utils.cpp"

int amount_of_displacements = 0;
int amount_of_comparisons = 0;

int select_Select(int* nums, int left, int right, int k, int size, int divide_size);
void select_swap(int* nums, int index1, int index2);
int select_partition(int* list, int left, int right, int pivotIndex, int n);
int select_partition_small(int* nums, int left, int right);

void swap(int* a, int* b)
{
    int t = *a;
    *a = *b;
    *b = t;
    amount_of_displacements += 3;
}

void select_swap(int* nums, int index1, int index2){
    int temp = nums[index1];
    nums[index1] = nums[index2];
    nums[index2] = temp;
    amount_of_displacements += 3; // 
}

int select_partition(int* list, int left, int right, int pivotIndex, int n){
    int pivotValue = list[pivotIndex];
    select_swap(list, pivotIndex, right); // move pivot to an end
    int storeIndex = left;
    // move all elements smaller than the pivot to the left of the pivot;
    for (int i = left; i <= right-1; i++){
        amount_of_comparisons+=2;
        if (list[i] < pivotValue){
            select_swap(list, storeIndex, i);
            storeIndex++;
        }
    }
    // Move all elements equal to the pivot right after the smaller elements
    int storeIndexEq = storeIndex;
    for (int i = storeIndex; i <= right-1; i++){
        amount_of_comparisons+=2;
        if(list[i] == pivotValue){
            select_swap(list, storeIndexEq, i);
            storeIndexEq++;
        }
    }
    select_swap(list, right, storeIndexEq); // Move pivot to its final place
    // Return location ofpivot considering the desired locaiton n
    amount_of_comparisons++;
    if (n < storeIndex) return storeIndex;
    amount_of_comparisons++;
    if (n <= storeIndexEq) return n;
    return storeIndexEq;  
}

int select_partition_small(int* nums, int left, int right){
    int i = left+1;
    amount_of_comparisons++;
    while (i <= right){
        int j = i;
        amount_of_comparisons+=2;
        while ( j > left && nums[j-1] > nums[j]){
            select_swap(nums, j-1, j);
            j--;
            amount_of_comparisons+=2;
        }
        i++;
        amount_of_comparisons++;
    }
    return (left+right)/2;
}

int select_pivot(int* nums, int left, int right, int size, int divide_size){
    // for 5 or less elements just get median
    amount_of_comparisons++;
    if (right - left < divide_size) return select_partition_small(nums, left, right);
    // otherwise move the medians of five-element subgroups to the first n/5 positions
    for ( int i = left; i <= right; i+= divide_size){
        amount_of_comparisons++;
        // get the median of the i'th five element subgroup
        int subRight = i+divide_size-1;
        amount_of_comparisons++;
        if (subRight > right) subRight = right;

        int median5 = select_partition_small(nums, i, subRight);
        select_swap(nums, median5, left + (i-left) / divide_size);
    }
    int mid = (right - left) / (divide_size*2) + left + 1;
    return select_Select(nums, left, left + (right-left)/divide_size, mid, size, divide_size);
}

int select_Select(int* nums, int left, int right, int k, int size, int divide_size){
    amount_of_comparisons++;
    while (1){
        amount_of_comparisons++;
        if (left == right) return left;

        int pivot_index = select_pivot(nums, left, right, size, divide_size);
        pivot_index = select_partition(nums, left, right, pivot_index, k);
        if (size < 50){
            preety_print_list(nums, size);
        }

        amount_of_comparisons++;
        if (k==pivot_index){
            return k; 
        } else if (k < pivot_index){
            amount_of_comparisons++;
            right = pivot_index - 1;
        } else {
            amount_of_comparisons++;
            left = pivot_index + 1;
        }
    }
}

int select_select(int* nums, int n, int k, int size, int divide_size){
    return select_Select(nums, 0, n-1, k-1, size, divide_size);
}

int Partition(int* nums, int low, int high){
    int pivot_index = select_pivot(nums, low, high, 100, 5);
    select_swap(nums, low, pivot_index);
    int pivot = nums[low];
    amount_of_displacements++; // slyszalem ze takie cos tez zapisujemy
    int leftwall = low+1;
    int temp; // only to swap

    for(int i = low + 1; i <= high; i++){
        amount_of_comparisons+=2; // warunek fora
        if (nums[i] < pivot) { 
            amount_of_displacements++; // jednoczesnie dobieramy wartosc z tablicy i porownujemy
            swap(&nums[i], &nums[leftwall]);
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
    amount_of_comparisons++;
    if (low >= high){
        return;
    }
    int copy_nums[n];
    copy(copy_nums, nums, n);
    int pivot_location = Partition(nums, low, high);
    if (n < 50)
        preety_print_list_with_colours(nums, n, copy_nums);
    quick_sort(nums, n, low, pivot_location-1);
    quick_sort(nums, n, pivot_location+1, high);
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
    std::cout << amount_of_comparisons  << " " << amount_of_displacements<< std::endl;
}