#pragma once
#include<vector>

struct node {
    int data;
    node* left;
    node* right;
};

class BST{
private:
    node* root;
    node* makeEmpty(node* t);
    node* insert(int x, node* t);
    node* findMin(node* t);
    node* remove(int x, node* t);
    void print(node* t, int indent, bool left_tree, std::vector<int> road);
    int height(node* t);
    long long amount_of_comparisons = 0;
    long long amount_of_read_and_displacements=0;
public:
    BST();
    ~BST();
    void insert(int k);
    void remove(int k);
    int height();
    void print();
    int leftmost();

    long long get_amount_of_comparisons();
    long long get_amount_of_displacements();
};