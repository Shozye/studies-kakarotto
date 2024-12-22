#include<iostream>
#include<random>
#include<vector>
#include<algorithm>
#include"utils.h"

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

void copy(int* arr1, int* arr2, int n){
    for(int i = 0; i< n ; i++){
        arr1[i] = arr2[i];
    }
}