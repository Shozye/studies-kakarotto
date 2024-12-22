#include<iostream>
#include"utils.cpp"

int amount_of_comparisons = 0;
int amount_of_displacements = 0;

int partition(int* arr, int low, int high, int* lp);
int select_Select(int* nums, int left, int right, int k, int size, int divide_size);
void select_swap(int* nums, int index1, int index2);
int select_partition(int* list, int left, int right, int pivotIndex, int n);
int select_partition_small(int* nums, int left, int right);

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

void swap(int* a, int* b)
{
    int temp = *a; 
    *a = *b;
    *b = temp;
    amount_of_displacements += 3; // swap to zawsze trzy są dla mnie
}
 
void DualPivotQuickSort(int* arr, int low, int high, int n)
{
    if (low < high) {
        amount_of_comparisons++; 
        int lp, rp;
        rp = partition(arr, low, high, &lp);
        DualPivotQuickSort(arr, low, lp - 1,n);
        DualPivotQuickSort(arr, lp + 1, rp - 1,n);
        DualPivotQuickSort(arr, rp + 1, high,n);
        if (n < 50){
            preety_print_list(arr, n);
        }
    }
}
 
int partition(int* arr, int low, int high, int* lp)
{
    // p is the left pivot, and q is the right pivot.
    int pivot_index1 = select_pivot(arr, low, high, 100, 5);
    swap(&arr[low], &arr[pivot_index1]);
    int pivot_index2 = select_pivot(arr, low+1, high, 100, 5);
    swap(&arr[high], &arr[pivot_index2]);

    if (arr[low] > arr[high]){
        amount_of_comparisons++; // jest porownanko
        swap(&arr[low], &arr[high]);
    }
    
    int j = low + 1;
    int g = high - 1, k = low + 1, p = arr[low], q = arr[high];
    while (k <= g) {
        amount_of_comparisons++;
        // if elements are less than the left pivot
        if (arr[k] < p) {
            amount_of_comparisons++;
            swap(&arr[k], &arr[j]);
            j++;
        }
 
        // if elements are greater than or equal
        // to the right pivot
        else if (arr[k] >= q) {
            amount_of_comparisons++; 
            while (arr[g] > q && k < g){
                amount_of_comparisons++; 
                g--;
            }
            swap(&arr[k], &arr[g]);
            g--;
            if (arr[k] < p) {
                amount_of_comparisons++; 
                swap(&arr[k], &arr[j]);
                j++;
            }
        }
        k++;
    }
    j--;
    g++;
 
    // bring pivots to their appropriate positions.
    swap(&arr[low], &arr[j]);
    swap(&arr[high], &arr[g]);
 
    // returning the indices of the pivots.
    *lp = j; // because we cannot return two elements
    // from a function.
 
    return g;
}

void sort(int* nums, int n){
    DualPivotQuickSort(nums, 0, n-1, n);
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