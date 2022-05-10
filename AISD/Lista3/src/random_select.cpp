#include<iostream>
#include"utils.cpp"

int amount_of_comparisons = 0;
int amount_of_displacements = 0;

void swap(int* nums, int index1, int index2){
    int temp = nums[index1];
    nums[index1] = nums[index2];
    nums[index2] = temp;
    amount_of_displacements += 3; // 
}

int Partition(int* nums, int low, int high, int n){
    int pivot = nums[high];
    int rightwall = low;

    amount_of_comparisons++;
    for(int j = low; j <= high-1; j++){
        amount_of_comparisons++;
        if (nums[j] <= pivot) {
            swap(nums, rightwall, j);
            rightwall++;
        }
        amount_of_comparisons++;
    }
    swap(nums, rightwall, high);

    return rightwall;
}

int RandPartition(int* nums, int p, int q, int n){
    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_int_distribution<int> dist{p, q};

    int r = dist(generator);
    swap(nums, r, q);
    return Partition(nums, p, q, n);
    // Returns index of pivot after RandPartition
}

int RandomSelect(int* nums, int p, int q, int i, int n){
    amount_of_comparisons++;
    if (p==q) return nums[p];
    int r = RandPartition(nums, p, q, n);

    if (n < 50) {
        preety_print_list(nums, n);
    }

    int k =     r-p+1;
    amount_of_comparisons++;
    if (k == i) return nums[r];
    amount_of_comparisons++;
    if (i < k)  return RandomSelect(nums, p  , r-1, i  , n);
    return RandomSelect(nums, r+1, q  , i-k, n);
}

int select(int* nums, int n, int i){
    return RandomSelect(nums, 0, n-1, i, n);
}

int main(){
    int n, i, divide_size;
    std::cin >> n;

    int nums[n];

    for(int i = 0; i < n; i++){
        std::cin >> nums[i];
    }
    std::cin >> i;
    std::cin >> divide_size;
    if(n < 50){
        std::cout << "Before searching:" << std::endl;
        preety_print_list(nums,n);
        std::cout << "During searching:" << std::endl;
    }
    int found = select(nums, n, i);
    if (n < 50){
        std::cout << "After searching:" << std::endl;
        preety_print_list(nums, n);
        std::cout << i << "-th smallest in nums is " << found << std::endl;
    }
    check_if_k_th_smallest(nums, n, i, found);
    std::cout << amount_of_comparisons << " " << amount_of_displacements << std::endl;

}