#include<iostream>
#include<random>
#include"utils.h"

int main(int argc, char** argv){
    int n = std::stoi(argv[1]);
    int* array = get_random_generated_array(n);

    std::cout << n << std::endl;
    print_list(array, n);

    delete[] array;
}
