#include<iostream>
#include<fstream>
#include<string>
#include<unordered_map>
#include<cmath>

void print_list_with_indexes(int* nums, int n){
    for(int i = 0; i < n; i++)
        if (nums[i] > 0)
            std::cout << i << " " << nums[i] << std::endl;
}

double entropy(std::ifstream* file){
    unsigned char byte = 0; 
    int size = 0; 
    int bytes[256] = {0}; 
    double sum = 0;
    while(!file -> eof()){
        byte = file->get();
        if(!file -> eof()){
            bytes[(int)byte]++;
            size++;
        }
    }
    for(int i = 0; i < 256; i++)
        if (bytes[i] != 0)
            sum += bytes[i] * std::log2l(bytes[i]);
    file -> seekg(0, std::ios::beg);
    return std::log2l(size) - (sum/(double)size);
}

double entropy(std::string filename){
    std::ifstream file (filename, std::ios::in | std::ios::binary);
    return entropy(&file);
}
