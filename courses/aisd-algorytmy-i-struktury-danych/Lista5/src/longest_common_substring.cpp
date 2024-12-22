#include<iostream>
#include"utils.h"
#include<stdexcept>
#include<vector>

bool print = false;
int amount_of_displacements = 0;
int amount_of_comparisons = 0;

int getindex(int i, int width, int j){
    return i*width+j;
}

int lcs(int* X, int* Y, int size){
    int m = size;
    int n = size;
    auto b = new int[(m+1)*(n+1)]; // uzywamy 1..m 1..n
    auto c = new int[(m+1)*(n+1)]; // uzywamy 0..m 0..n


    for(int i = 1; i <= m; i++){
        c[getindex(i, size, 0)] = 0;
    }
    for (int j = 0; j <=n ; j++){
        c[getindex(0, size, j)] = 0;
    }
    
    for(int i = 1; i <= m; i++){
        for(int j = 1; j<=n;j++){
            if(X[i-1] == Y[j-1]){
                amount_of_comparisons += 1;
                amount_of_displacements += 1;
                c[getindex(i, size, j)] = c[getindex(i-1, size, j-1)] + 1;
                b[getindex(i, size, j)] = 2; // lewo gora
            }
            else if(c[getindex(i-1, size, j)] >= c[getindex(i, size, j-1)]){
                amount_of_comparisons += 2;
                amount_of_displacements += 1;
                c[getindex(i, size, j)] = c[getindex(i-1, size, j)];
                b[getindex(i, size, j)] = 1; // gora
            }
            else if (c[getindex(i, size, j)] = c[getindex(i, size, j-1)]){
                amount_of_comparisons += 3;
                b[getindex(i, size, j)] = 0; // lewo
            }
            else amount_of_comparisons += 3;
        }
    }

    if(print){
        std::vector<int> prints;
        int i = size;
        int j = size;
        while (i >= 0 and j>=0){
            if(b[getindex(i, size, j)] == 2){
                prints.push_back(X[i-1]);
                i--;
                j--;
            }
            else if(b[getindex(i, size, j)] == 1) i--;
            else j--;
        }

        std::cout << "Substring: ";
        for(int k = prints.size()-1; k>=0; k--){
            std::cout << prints[k] << " ";
        }
        std::cout << std::endl;
    }

    return c[getindex(m, size, n)];
}

int main(int argc, char** argv){
    if (argc > 1){
        print=true;
    }

    int n;
    std::cin >> n;
    if (n%2 != 0) 
        throw std::invalid_argument("Input list size should be divisible by 2");
    int size = n/2;
    int t1[size];
    int t2[size];

    for(int i = 0; i < size; i++){
        std::cin >> t1[i];
        std::cin >> t2[i];
    }
    if(print){
        std::cout << "Array 1: ";
        preety_print_list(t1, size);
        std::cout << "Array 2: ";
        preety_print_list(t2, size);
    }
    int lcs_len = lcs(t1, t2, size);
    if(print){
        std::cout << "LCS: " << lcs_len << std::endl;
    }
    std::cout << amount_of_displacements << " " << amount_of_comparisons << std::endl;

}