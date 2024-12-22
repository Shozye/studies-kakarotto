#include"utils.cpp"
#include <thread>
#include <algorithm>
#include <chrono>
#include <iostream>
#include <vector>
#include <random>

using namespace std::chrono;

int amount_of_comparisons = 0;
int amount_of_displacements = 0;

int binarySearch(int arr[], int l, int r, int x)
{
    amount_of_comparisons++;
    if (r >= l) {
        int mid = l + (r - l) / 2;
        amount_of_comparisons++;
        if (arr[mid] == x)
            return 1;
        amount_of_comparisons++;
        if (arr[mid] > x)
            return binarySearch(arr, l, mid - 1, x);
        return binarySearch(arr, mid + 1, r, x);
    }
    return -1;
}
 
int main(int argc, char** argv){
    int n, element_to_search;
    std::cin >> n;

    int nums[n];

    for(int i = 0; i < n; i++){
        std::cin >> nums[i];
    }
    element_to_search = std::stoi(argv[1]);

    if (n < 50) preety_print_list(nums,n);

    if (element_to_search == -2){
        std::random_device rd;
        std::mt19937 generator(rd());
        std::uniform_int_distribution<int> dist{0, n-1};
        element_to_search = nums[dist(generator)];
    }
    auto start = high_resolution_clock::now();
    int found;
    double AMOUNT = 1000.0;
    for(int i = 0; i < AMOUNT; i++){
        found = binarySearch(nums, 0, n-1, element_to_search);
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<microseconds>(stop - start);
 
    std::cout << found << " " << amount_of_comparisons / AMOUNT << " " << duration.count() / (AMOUNT*1000000)  << std::endl;

}