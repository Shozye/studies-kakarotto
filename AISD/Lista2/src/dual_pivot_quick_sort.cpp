#include<iostream>
#include"utils.cpp"

int amount_of_comparisons = 0;
int amount_of_displacements = 0;

int partition(int* arr, int low, int high, int* lp);


void swap(int* a, int* b)
{
    int temp = *a; 
    *a = *b;
    *b = temp;
    amount_of_displacements += 3; // swap to zawsze trzy są dla mnie
}
 
void DualPivotQuickSort(int* arr, int low, int high)
{
    if (low < high) {
        amount_of_comparisons++; // jest porownanko
        // lp means left pivot, and rp means right pivot.
        int lp, rp;
        rp = partition(arr, low, high, &lp);
        DualPivotQuickSort(arr, low, lp - 1);
        DualPivotQuickSort(arr, lp + 1, rp - 1);
        DualPivotQuickSort(arr, rp + 1, high);
    }
}
 
int partition(int* arr, int low, int high, int* lp)
{
    if (arr[low] > arr[high]){
        amount_of_comparisons++; // jest porownanko
        swap(&arr[low], &arr[high]);
    }
    // p is the left pivot, and q is the right pivot.
    int j = low + 1;
    int g = high - 1, k = low + 1, p = arr[low], q = arr[high];
    while (k <= g) {
        amount_of_comparisons++; // jest porownanko
        // if elements are less than the left pivot
        if (arr[k] < p) {
            amount_of_comparisons++; // jest porownanko
            swap(&arr[k], &arr[j]);
            j++;
        }
 
        // if elements are greater than or equal
        // to the right pivot
        else if (arr[k] >= q) {
            amount_of_comparisons++; // jest porownanko
            while (arr[g] > q && k < g){
                amount_of_comparisons++; // jest porownanko
                g--;
            }
            swap(&arr[k], &arr[g]);
            g--;
            if (arr[k] < p) {
                amount_of_comparisons++; // jest porownanko
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
    DualPivotQuickSort(nums, 0, n-1);
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