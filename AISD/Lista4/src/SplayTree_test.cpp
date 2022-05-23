#include<iostream>
#include"SplayTree.h"
#include<algorithm>
#include"utils.h"
#include<string>

int main(int argc, char** argv){
    int n;
    bool should_print = false;
    int height = 0;
    int max_height = 0;
    int max_comparisons_diff = 0;
    int max_displacements_diff = 0;
    std::cin >> n;
    int delete_arr[n];
    for (int i = 0; i < n ; i++){
        std::cin >> delete_arr[i];
    }

    SplayTree tree = SplayTree();
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
        int prev_comparisons = tree.get_amount_of_comparisons();
        int prev_displacements = tree.get_amount_of_displacements();

        tree.insert(source_arr[i]);

        int comparisons_diff = tree.get_amount_of_comparisons(); - prev_comparisons;
        int displacements_diff = tree.get_amount_of_displacements(); - prev_displacements;
        int h = tree.height();
        height += h;
        if(h > max_height) max_height = h;
        if(comparisons_diff > max_comparisons_diff)
            max_comparisons_diff = comparisons_diff;
        if(displacements_diff > max_displacements_diff)
            max_displacements_diff = displacements_diff;

        if (should_print){
            tree.print();
            std::cout <<"HEIGHT: " << tree.height() << std::endl << std::endl;
        }
    }

    if(should_print)
        std::cout << "======= REMOVING ======" << std::endl;
    for(int i = 0; i < n; i++){
        int prev_comparisons = tree.get_amount_of_comparisons();
        int prev_displacements = tree.get_amount_of_displacements();

        tree.deleteNode(delete_arr[i]);

        int comparisons_diff = tree.get_amount_of_comparisons(); - prev_comparisons;
        int displacements_diff = tree.get_amount_of_displacements(); - prev_displacements;
        int h = tree.height();
        height += h;
        if(h > max_height) max_height = h;
        if(comparisons_diff > max_comparisons_diff)
            max_comparisons_diff = comparisons_diff;
        if(displacements_diff > max_displacements_diff)
            max_displacements_diff = displacements_diff;

        if (should_print){
            tree.print();
            std::cout <<"HEIGHT: " << tree.height() << std::endl << std::endl;
        }
    }
    std::cout << ((double) tree.get_amount_of_comparisons() / (double) (2*n)) << " ";
    std::cout << ((double) tree.get_amount_of_displacements() / (double) (2*n))<< " ";
    std::cout << ((double) height / (double) (2*n)) << " ";
    std::cout << max_comparisons_diff << " ";
    std::cout << max_displacements_diff << " ";
    std::cout << max_height << std::endl;
}