#include<iostream>
#include<string>
#include<fstream>

int main(int argc, char** argv){
    std::string filename = argv[1];
    std::string filepath = "tests/" + filename;
    std::string new_filepath = "encoded/" + filename + ".mp";
    std::ifstream file (filepath, std::ios::in | std::ios::binary);
}