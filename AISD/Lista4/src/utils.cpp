#include<iostream>
#include<random>
#include<vector>
#include<algorithm>

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

void print_indent(int n){
    for (int i =0; i < n; i++){
        std::cout << "  ";
    }
}

void copy_list(int* source, int* target, int n){
    for(int i = 0; i < n; i++){
        target[i] = source[i];
    }
}