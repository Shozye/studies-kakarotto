#include<iostream>

void print_list(int* arr, int n){
    for (int i = 0 ; i < n ; i ++ ){
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

void bin(int num, int binary[8]){
    // num should be ranged 0 ... 255
    for(int i = 7; i >=0; i--){
        binary[i] = num%2;
        num /= 2;
    }
}

