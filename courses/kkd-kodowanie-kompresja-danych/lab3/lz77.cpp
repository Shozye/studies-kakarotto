#include<string>
#include<iostream>
#include<chrono>
#include<fstream>
#include<cmath>
#include<filesystem>
#include<vector>
#include<algorithm>


int filesize(std::string filename){
    std::filesystem::path p{filename};
    return std::filesystem::file_size(p);
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

void end_information(std::string filename_start, std::string filename_compressed){
    int fs_size = filesize(filename_start);
    int fc_size = filesize(filename_compressed);
    double fs_entropy = entropy(filename_start);
    double fc_entropy = entropy(filename_compressed);
    std::cout << "Długość kodowanego pliku to " << fs_size << std::endl;
    std::cout << "Dlugosc kodu to " << fc_size << std::endl;
    std::cout << "Stopien kompresji: " << (double) fc_size / (double) fs_size << std::endl;
    std::cout << "Entropia kodowanego tekstu: " << fs_entropy << std::endl;
    std::cout << "Entropia uzyskanego: " << fc_entropy << std::endl;
}




void compress(std::string filename, std::string file_dir, std::string output_dir){
    std::ifstream infile (file_dir + filename, std::ios::in | std::ios::binary);
    std::ofstream outfile (output_dir + filename, std::ios::out | std::ios::binary);
    char* plaintext = new char[2000000];
    int dict_buffer_ptr_start = 0;
    int dict_buffer_ptr_end = 0;
    int coding_buffer_ptr_start = 0;
    int coding_buffer_ptr_end = 256;
    int file_size = 0;
    while(!infile.eof()){
        plaintext[file_size] = infile.get();
        if(!infile.eof()){
            file_size++;
        }
    }

    while (dict_buffer_ptr_end != file_size){
        std::vector<char> longest_prefix;
        int prefix_index = -1;

        for (int i = coding_buffer_ptr_start; i < coding_buffer_ptr_end; i++){
            char letter = plaintext[i];

            std::vector<char> temp_prefix = longest_prefix;
            temp_prefix.push_back(letter);
            int len = temp_prefix.size();

            int index = -1;
            for(int j = dict_buffer_ptr_start; j < dict_buffer_ptr_end - len + 1; j++){
                bool good = true;
                for (int prefix_iter = 0; prefix_iter < len; prefix_iter++){
                    if (temp_prefix[prefix_iter] != plaintext[j+prefix_iter]){
                        good = false;
                        break;
                    }
                }
                if(good){
                    index = j;
                    break;
                }
            }
            if (index == -1){
                break;
            }
            prefix_index = index;
            longest_prefix = temp_prefix;
        }
        if (prefix_index == -1){
            char byte_to_write = plaintext[coding_buffer_ptr_start];
            outfile.put(0);
            outfile.put(byte_to_write);

            coding_buffer_ptr_start = std::min(coding_buffer_ptr_start + 1, file_size);
            coding_buffer_ptr_end = std::min(coding_buffer_ptr_end + 1, file_size);
            dict_buffer_ptr_end += 1;
            dict_buffer_ptr_start = std::max(dict_buffer_ptr_end - 255, 0);
        }
        else{
            int j = coding_buffer_ptr_start - prefix_index;
            int l = longest_prefix.size();
            outfile.put(j);
            outfile.put(l);

            coding_buffer_ptr_start = std::min((int)(coding_buffer_ptr_start + longest_prefix.size()), file_size);
            coding_buffer_ptr_end = std::min((int)(coding_buffer_ptr_end + longest_prefix.size()), file_size);
            dict_buffer_ptr_end += longest_prefix.size();
            dict_buffer_ptr_start = std::max(dict_buffer_ptr_end - 255, 0);
        }
    }
    infile.close();
    outfile.close();
}

void decompress(std::string filename, std::string file_dir, std::string output_dir){
    std::ifstream infile (file_dir + filename, std::ios::in | std::ios::binary);
    std::ofstream outfile (output_dir + filename, std::ios::out | std::ios::binary);
    std::vector<char> plaintext;

    while (!infile.eof()){
        unsigned char j = infile.get();
        if (infile.eof()){
            break;
        }
        unsigned char l = infile.get();
        if (j==0){
            plaintext.push_back(l);
        }
        else{
            std::vector<char> to_add;
            for (int i=-j; i < -j+l; i++){
                to_add.push_back(plaintext[plaintext.size() + i]);
            }
            for (int i = 0; i < to_add.size(); i++){
                plaintext.push_back(to_add[i]);
         
            }
        }
    }
    for ( int i = 0; i < plaintext.size(); i++){
        outfile.put(plaintext[i]);
    }
    infile.close();
    outfile.close();
}

void tests(){
    std::string filenames[] = {"pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt",
                             "test1.bin","test2.bin","test3.bin"};
    //std::string filenames[] = {"my_test1.txt", "my_test2.txt", "my_test3.txt", "my_test4.txt"};
    for (auto filename : filenames){
        auto start_time = std::chrono::high_resolution_clock::now();
        std::cout << "\nStart compressing " << filename << std::endl;
        compress(filename, "files/", "compressed/");
        auto compress_time = std::chrono::high_resolution_clock::now();
        end_information("files/" + filename, "compressed/" + filename);
        std::cout << "Compression of " << filename << " took " << std::chrono::duration_cast<std::chrono::microseconds>(compress_time - start_time).count() << " microseconds" << std::endl;
        decompress(filename, "compressed/", "decompressed/");
        auto decompress_time = std::chrono::high_resolution_clock::now();
        std::cout << "Decompression of " << filename << " took " << std::chrono::duration_cast<std::chrono::microseconds>(decompress_time - compress_time).count() << " microseconds" << std::endl;
    }               
}

int main(){
    tests();
}