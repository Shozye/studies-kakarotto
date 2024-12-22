#include<iostream>
#include<random>
#include<vector>
#include<algorithm>

int* get_random_generated_array(int n){
    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_int_distribution<int> dist{0, 2*n-1};

    int* array = new int[n];
    for(int i = 0 ; i < n; i++) {
        array[i] = dist(generator);
    }

    return array;
}

void print_list(int* array, int n){
    for (int i = 0 ; i < n; i ++){
        std::cout << array[i] << "\n";
    }
}

void preety_print_list(int* array, int n){
    for (int i = 0; i < n; i++){
        if (array[i] < 10){
            std::cout << 0;
        }
        std::cout << array[i] << " ";
    }
    std::cout<<std::endl;
}


void preety_print_list_with_colours(int* array, int n, int *previous_array){
    std::vector<int> to_colour;
    for(int i = 0; i < n; i ++){
        if (previous_array[i] != array[i]){
            to_colour.push_back(i);
        }
    }

    for (int i = 0; i < n; i++){
        if(std::find(to_colour.begin(), to_colour.end(), i) != to_colour.end()){
            std::cout << "\033[1;31m";
        }
        if (array[i] < 10){
            std::cout << 0;
        }
        std::cout << array[i] << " ";
        std::cout << "\033[0m";
    }
    std::cout<<std::endl;
}

void check_if_list_sorted(int* array, int n){
    bool sorted = true;
    for(int i = 0; i < n-1; i++){
        if (array[i+1] < array[i]){
            std::cout << "List is not sorted for [" << array[i+1] << "] >= [" << array[i] <<"]"<< std::endl;
            return;
        }
    }
}

void check_if_k_th_smallest(int *array, int n, int k, int num){
    int amount_of_lower = 0;
    int amount_of_equal = 0;
    int lower[n];
    int lower_index = 0;
    int equal[n];
    int equal_index = 0;
    for(int i = 0; i < n; i ++){
        if (array[i] < num) {
            amount_of_lower++;
            lower[lower_index] = array[i];
            lower_index++;
        }
        if (array[i] == num) {
            amount_of_equal++;
            equal[equal_index] = array[i];
            equal_index++;
        }
    }
    if(!(amount_of_lower + 1 <= k && amount_of_lower + amount_of_equal >=k)){
        std::cout << "num {" << num << "} is not " << k << "-th element of array" << std::endl;
        for(int i = 0; i < equal_index; i++){
            std::cout << equal[i] << " ";
        }
        std::cout << std::endl;
        for(int i = 0; i < lower_index; i++){
            std::cout << lower[i] << " ";
        }
        std::cout << std::endl;
    }
}

void copy(int* arr1, int* arr2, int n){
    for(int i = 0; i< n ; i++){
        arr1[i] = arr2[i];
    }
}