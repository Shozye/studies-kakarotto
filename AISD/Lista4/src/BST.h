#pragma once
#include<vector>

class BST{
private:
    int value;
    BST* left;
    BST* right;
    bool empty;
public:
    BST();
    ~BST();
    void insert(int k);
    void del(int k);
    int height();
    void print(int indent, bool left_tree, std::vector<int> road);
    void print();
    void inorder();
    int leftmost();
    
    int get_amount_of_comparisons();
    int get_amount_of_displacements();
};