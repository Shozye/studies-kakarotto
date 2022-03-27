#include<iostream>
#include<random>
#include"utils.cpp"
#include<algorithm>


int main(int argc, char** argv){
    int n = std::stoi(argv[1]);
    int* array = get_random_generated_array(n);
    std::sort(array, array + n, std::greater<int>());

    std::cout << n << std::endl;
    print_list(array, n);

    delete[] array;
}
