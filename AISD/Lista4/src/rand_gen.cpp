#include<iostream>
#include<random>
#include"utils.h"
#include"stdexcept"

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

bool in(int num, int* array, int size){
    for(int i = 0; i < size; i++){
        if (array[i] == num) return true;
    }
    return false;
}

int* get_distinct_random_generated_array(int n){
    std::random_device rd;
    std::mt19937 generator(rd());
    std::uniform_int_distribution<int> dist{0, 2*n-1};
    int size = 0;
    int* array = new int[n];
    int* map = new int[2*n];
    for(int i = 0 ; i < 2*n; i++) map[i] = 0;
    while(size != n){
        int num = dist(generator);
        if (map[num] == 1) continue;
        map[num] = 1;
        array[size] = num;
        size++;
    }
    return array; 
}


int main(int argc, char** argv){
    int n = std::stoi(argv[1]);
    int* array;
    if (argc > 2){
        array = get_distinct_random_generated_array(n);
        if(!is_distinct_array(array, n))
            throw std::logic_error("Not distinct array"); 
    }
    else
        array = get_random_generated_array(n);

    std::cout << n << std::endl;
    print_list(array, n);
    delete[] array;
}
