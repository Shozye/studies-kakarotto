#ifndef RED_BLACK_TREE_H
#define RED_BLACK_TREE_H

#include <iostream>
#include <vector>

typedef struct Node
{
    int key;               
    char color;            
    char pad[3];            
    struct Node* left;      
    struct Node* right;   
    struct Node* parent; 
   
} Node;

class Red_black_tree{
public:
    Red_black_tree();
    Node* new_Node(int key);                
    Node* tree_minimum(Node* node);         
    Node* tree_maksimum(Node* node);        
    Node* tree_successor(Node* node);       
    Node* tree_search(Node* node, int key);
    void  free_tree(Node* node);
    void  left_rotate(Node* node);
    void  right_rotate(Node* node);
    void  delete_Node(int key);
    void  delete_fixup(Node* node);
    void  transplant(Node* u, Node* v);
    void  insert_Node(int key); 
    void  insert_fixup(Node* node);
    int   tree_height(void);


    int height();
    int height(Node* root);;
    void print_indent(int indent, std::vector<int> road);
	void print();
    void print(Node* root, int indent, bool left_tree, std::vector<int> road);

    long get_amount_of_comparisons();
    long get_amount_of_displacements();
};
#endif