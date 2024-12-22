#include<iostream>
#include"BST.h"
#include<algorithm>
#include"utils.h"
#include<string>

int main(int argc, char** argv){
    int n;
    bool should_print = false;
    long long height = 0;
    long long max_height = 0;
    long long max_comparisons_diff = 0;
    long long max_displacements_diff = 0;
    std::cin >> n;
    int* delete_arr = new int[n];
    for (int i = 0; i < n ; i++){
        std::cin >> delete_arr[i];
    }

    BST* tree = new BST();
    int* source_arr = new int[n];
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
        long long prev_comparisons = tree->get_amount_of_comparisons();
        long long prev_displacements = tree->get_amount_of_displacements();

        tree->insert(source_arr[i]);

        long long comparisons_diff = tree->get_amount_of_comparisons() - prev_comparisons;
        long long displacements_diff = tree->get_amount_of_displacements() - prev_displacements;
        long long h = tree->height();
        height += h;
        if(h > max_height) max_height = h;
        if(comparisons_diff > max_comparisons_diff)
            max_comparisons_diff = comparisons_diff;
        if(displacements_diff > max_displacements_diff)
            max_displacements_diff = displacements_diff;

        if (should_print){
            std::cout << "Insert " << source_arr[i] << std::endl << std::endl;
            tree->print();
            std::cout <<"HEIGHT: " << tree->height() << std::endl << std::endl;
        }
    }

    if(should_print)
        std::cout << "======= REMOVING ======" << std::endl;
    for(int i = 0; i < n; i++){
        long long prev_comparisons = tree->get_amount_of_comparisons();
        long long prev_displacements = tree->get_amount_of_displacements();

        tree->remove(delete_arr[i]);

        long long comparisons_diff = tree->get_amount_of_comparisons() - prev_comparisons;
        long long displacements_diff = tree->get_amount_of_displacements() - prev_displacements;
        long long h = tree->height();
        height += h;
        if(h > max_height) max_height = h;
        if(comparisons_diff > max_comparisons_diff)
            max_comparisons_diff = comparisons_diff;
        if(displacements_diff > max_displacements_diff)
            max_displacements_diff = displacements_diff;

        if (should_print){
            std::cout << "Delete " << delete_arr[i] << std::endl << std::endl;
            tree->print();
            std::cout <<"HEIGHT: " << tree->height() << std::endl << std::endl;
        }
    }
    std::cout << ((double) tree->get_amount_of_comparisons() / (double) (2*n)) << " ";
    std::cout << ((double) tree->get_amount_of_displacements() / (double) (2*n))<< " ";
    std::cout << ((double) height / (double) (2*n)) << " ";
    std::cout << max_comparisons_diff << " ";
    std::cout << max_displacements_diff << " ";
    std::cout << max_height << std::endl;

}