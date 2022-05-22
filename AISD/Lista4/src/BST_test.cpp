#include<iostream>
#include"BST.h"
#include<algorithm>
#include"utils.h"
#include<string>

int main(int argc, char** argv){
    int n;
    bool should_print = false;
    std::cin >> n;
    int delete_arr[n];
    for (int i = 0; i < n ; i++){
        std::cin >> delete_arr[i];
    }

    BST tree = BST();
    int source_arr[n];
    copy_list(delete_arr, source_arr, n);

    if (argc >= 2 && argv[1] == std::string("ASCENDING")){ // ASCENDING MODE
        std::sort(source_arr, source_arr+n);
    }

    if (argc >= 3 && argv[2] == std::string("PRINT")){ // PRINT MODE
        should_print = true;
    }

    if(should_print)
        std::cout << "========== INSERTING ======== " << std::endl;
    for(int i = 0; i < n; i++){
        tree.insert(source_arr[i]);
        if (should_print){
            tree.print();
            std::cout <<"HEIGHT: " << tree.height() << std::endl << std::endl;
        }
    }

    if(should_print)
        std::cout << "======= REMOVING ======" << std::endl;
    for(int i = 0; i < n; i++){
        tree.del(delete_arr[i]);
        if (should_print){
            tree.print();
            std::cout <<"HEIGHT: " << tree.height() << std::endl << std::endl;
        }
    }

    std::cout << tree.amount_of_comparisons << " " << tree.amount_of_read_and_displacements << std::endl;
}