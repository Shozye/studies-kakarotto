#include<iostream>
#include<fstream>
#include<string>
#include<unordered_map>
#include<cmath>

double calculate_one_byte_entropy(std::ifstream* myfile){
    int byte_counter[256] = {0};
    int size=0;
    char letter;

    while(myfile -> get(letter)){
        int val = letter + 127;
        byte_counter[val]++;
        size++;
    }
    // H = log2l(size) - 1/size * (sum for i=1..n of Ai*log2l(Ai))
    double log2lsize = std::log2l(size);
    double sum = 0;

    for(int i = 0; i < 256; i++){
        if (byte_counter[i] != 0)
            sum += byte_counter[i] * std::log2l(byte_counter[i]); 
    }
    double sum_divided_by_size = sum/(double)size;
    return log2lsize - sum_divided_by_size;
}

double calc_conditional_entropy(std::ifstream* myfile){
    int double_byte_counter[256][256];
    for(int i = 0; i < 256; i++){
        for (int j = 0; j < 256; j++){
            double_byte_counter[i][j] = 0;
        }
    }
    int byte_counter[256] = {0};
    char letter;
    int previous = 127;
    int symbol_amount = 0;
    while(myfile -> get(letter)){
        int val = letter + 127;
        byte_counter[val]++;
        double_byte_counter[previous][val]++;

        previous = val;
        symbol_amount++;
    }
    double HYX = 0;
    for (int x=0; x < 256; x++){
        for(int y=0; y < 256; y++){
            if (byte_counter[x] != 0 && double_byte_counter[x][y] != 0){
                double pxy = double_byte_counter[x][y] / (double)symbol_amount;
                double logpxypx = std::log2l(((double)double_byte_counter[x][y])/((double)byte_counter[x]));
                HYX += pxy*logpxypx;
                }
        }
    }
    if (HYX == 0)
        return HYX;
    return -1*HYX;
}

double abs(double x){
    if (x < 0){
        return -1 * x;
    }
    return x;
}

int main(int argc, char* argv[]){
    if (argc < 2){
        std::cout << "add filename argument" << std::endl;
        return 1;
    }
    std::ifstream myfile (argv[1], std::ios::in | std::ios::binary);
    if (!myfile.is_open()) {
        std::cerr << "Could not open the file - '"
             << argv[1] << "'" << std::endl;
        return 1;
    }
    double entropy = calculate_one_byte_entropy(&myfile);
    std::cout << "ENTROPY := " << entropy << std::endl;

    std::ifstream myfile2 (argv[1], std::ios::in | std::ios::binary);
    if (!myfile2.is_open()) {
        std::cerr << "Could not open the file - '"
             << argv[1] << "'" << std::endl;
        return 1;
    }
    double cond_entropy = calc_conditional_entropy(&myfile2);
    std::cout << "COND_ENTROPY := " << cond_entropy << std::endl;
    std::cout << "DIFF := " << abs(cond_entropy - entropy)<<std::endl;
}