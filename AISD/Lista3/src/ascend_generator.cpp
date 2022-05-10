#include<iostream>
#include<random>
#include"utils.cpp"
#include<algorithm>


int main(int argc, char** argv){
    int n = std::stoi(argv[1]);
    int i = std::stoi(argv[2]);
    int divide_size = std::stoi(argv[3]);
    int* array = get_random_generated_array(n);
    std::sort(array, array + n);

    std::cout << n << std::endl;
    print_list(array, n);
    std::cout << i << std::endl;
    std::cout << divide_size << std::endl;
    delete[] array;
}
