#include"utils.h"
#include<string>
int main(int argc, char** argv){
    std::string filenames[4] = {"tests/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt",
                                "tests/test1.bin",
                                "tests/test2.bin",
                                "tests/test3.bin",
                                };
    for(int i = 0; i < 4; i++){
        std::cout << "Entropy of " << filenames[i] << " is " <<  entropy(filenames[i]) << std::endl; 
    }
    return 0;
}