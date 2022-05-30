#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "Red_black_tree.h"
#include<algorithm>
#include"utils.h"

static Node* T_nil = NULL;
static Node* root = NULL;

Node* Red_black_tree::new_Node(int key)
{
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->key = key;
    newNode->color = 'B';
    newNode->parent = T_nil;
    newNode->left = T_nil;
    newNode->right = T_nil;
 
    return newNode;
}

Red_black_tree::Red_black_tree(){}

long amount_of_comparisons=0;
long amount_of_read_and_displacements=0;

long Red_black_tree::get_amount_of_comparisons(){
    return amount_of_comparisons;
}

long Red_black_tree::get_amount_of_displacements(){
    return amount_of_read_and_displacements;
}

void Red_black_tree::left_rotate(Node* x)
{
    amount_of_read_and_displacements += 2;
    Node* y = x->right;
    x->right = y->left;

    amount_of_read_and_displacements++;
    if (y->left != T_nil)
    {
        amount_of_read_and_displacements++;
        y->left->parent = x;
    }
    amount_of_read_and_displacements++;
    y->parent = x->parent; 
    amount_of_read_and_displacements++;
    if (x->parent == T_nil)
    {
        amount_of_read_and_displacements++;
        root = y;
    }
    else if (x == x->parent->left)
    {
        amount_of_read_and_displacements += 2;
        x->parent->left = y;
    }
    else if (x == x->parent->right)
    {
        amount_of_read_and_displacements += 2;
        x->parent->right = y;
    }
    amount_of_read_and_displacements += 2;
    y->left = x;
    x->parent = y;
}

void Red_black_tree::right_rotate(Node* x){
    amount_of_read_and_displacements += 3;
    Node* y;
    y = x->left; 
    x->left = y->right;

    amount_of_read_and_displacements++;
    if (y->right != T_nil)
    {
        amount_of_read_and_displacements++;
        y->right->parent = x;
    }
    amount_of_read_and_displacements++;
    y->parent = x->parent;
    amount_of_read_and_displacements++;
    if (x->parent == T_nil)
    {
        amount_of_read_and_displacements++;
        root = y;
    }
    else if (x == x->parent->right)
    {
        amount_of_read_and_displacements += 2;
        x->parent->right = y;
    }
    else if (x == x->parent->left)
    {
        amount_of_read_and_displacements += 3;
        x->parent->left = y;
    }
    y->right = x;
    x->parent = y;
}

void Red_black_tree::insert_Node(int key){

    amount_of_read_and_displacements++;
    if (root == NULL)
    {   
        root = new_Node(key);
        return;
    }
    
    Node* z = new_Node(key);
    Node* y = T_nil;
    Node* x = root;
    amount_of_read_and_displacements += 4;
    while (x != T_nil)
    {
        amount_of_read_and_displacements++;
        y = x;
        amount_of_comparisons += 1;
        if (z->key < x->key)
        {
            amount_of_read_and_displacements++;
            x = x->left;
        }
        else
        {
            amount_of_read_and_displacements++;
            x = x->right;
        }
    }
    amount_of_read_and_displacements++;
    z->parent = y;
    amount_of_read_and_displacements++;
    if (y == T_nil)
    {
        amount_of_read_and_displacements++;
        root = z;
    }
    else if (z->key < y->key)
    {
        amount_of_comparisons += 1;
        amount_of_read_and_displacements++;
        y->left = z;
    }
    else
    {
        amount_of_comparisons += 1;
        amount_of_read_and_displacements++;
        y->right = z;
    }

    amount_of_read_and_displacements += 2;
    z->left = T_nil;
    z->right = T_nil;
    z->color = 'R';
    
    insert_fixup(z);
} 

void Red_black_tree::insert_fixup(Node* z)
{ 
    amount_of_read_and_displacements++;
    Node* y = NULL;
    while (z->parent->color == 'R')
    {
        amount_of_read_and_displacements++;
        if (z->parent == z->parent->parent->left)
        {
            amount_of_read_and_displacements++;
            y = z->parent->parent->right;
            if (y->color == 'R')
            {
                z->parent->color = 'B';                 
                y->color = 'B';                         
                z->parent->parent->color = 'R';  
                amount_of_read_and_displacements++;        
                z = z->parent->parent;                  
            }
            else 
            {
                amount_of_read_and_displacements++;
                if (z == z->parent->right)
                {
                    amount_of_read_and_displacements++;
                    z = z->parent;                     
                    left_rotate(z);                
                }
                z->parent->color = 'B';              
                z->parent->parent->color = 'R';      
                right_rotate(z->parent->parent);
            }
        } 
        else if (z->parent == z->parent->parent->right)
        {
            amount_of_read_and_displacements += 2;
            y = z->parent->parent->left;
            if (y->color == 'R')
            {
                z->parent->color = 'B';                 
                y->color = 'B';                         
                z->parent->parent->color = 'R';     
                amount_of_read_and_displacements++;   
                z = z->parent->parent;                 
            }
            else 
            {
                amount_of_read_and_displacements++;
                if (z == z->parent->left)
                {
                    amount_of_read_and_displacements++;
                    z = z->parent;                     
                    right_rotate(z);              
                }
                z->parent->color = 'B';                
                z->parent->parent->color = 'R';  
                left_rotate(z->parent->parent); 
            }
        }
        
    }
    root->color = 'B'; 
}

void Red_black_tree::transplant(Node* u, Node* v)
{
    amount_of_read_and_displacements++;
    if (u->parent == T_nil)
    {
        amount_of_read_and_displacements++;
        root = v;
    }
    else if (u == u->parent->left)
    {
        amount_of_read_and_displacements += 2;
        u->parent->left = v;
    }
    else
    {
        amount_of_read_and_displacements += 2;
        u->parent->right = v;
    }
    amount_of_read_and_displacements++;
    v->parent = u->parent;
}

Node* Red_black_tree::tree_search(Node* node, int key){

    amount_of_read_and_displacements++;
    if (node == T_nil || key == node->key)
        return node;  
    if (key < node->key)
        return tree_search(node->left, key);
    else{
        return tree_search(node->right, key);
    }
}

Node* Red_black_tree::tree_minimum(Node* node){
    Node* x = node; 
    amount_of_read_and_displacements += 1;
    while(x->left != T_nil){
        amount_of_read_and_displacements+=2;
        x = x->left;
    } 
    return x;
}

void Red_black_tree::delete_Node(int key)
{
    Node* z = tree_search(root, key);
    amount_of_read_and_displacements++;
    if (z == T_nil)
        return;
    
    Node* y = z;
    Node* x = NULL;
    char y_original_color = y->color;

    amount_of_read_and_displacements++;
    if (z->left == T_nil)
    {
        amount_of_read_and_displacements++;
        x = z->right;
        transplant(z, z->right);
    }
    else if(z->right == T_nil)
    {
        amount_of_read_and_displacements += 2;
        x = z->left;
        transplant(z, z->left);
    }
    else
    {
        amount_of_read_and_displacements += 2;

        amount_of_read_and_displacements += 1;
        y = tree_minimum(z->right);
        y_original_color = y->color;
        x = y->right;

        amount_of_read_and_displacements++;
        if (y->parent == z)
        {
            amount_of_read_and_displacements++;
            x->parent = y;
        }
        else
        {
            transplant(y, y->right);
            amount_of_read_and_displacements += 2;
            y->right = z->right;
            y->right->parent = y;
        }
        transplant(z, y);
        amount_of_read_and_displacements += 2;
        y->left = z->left;
        y->left->parent = y;
        y->color = z->color;
    }
    if (y_original_color == 'B')
    {
        delete_fixup(x);
    }
    free(z);
}

void Red_black_tree::delete_fixup(Node* x)
{
    Node* w = NULL;

    amount_of_read_and_displacements++;
    while (x != root && x->color == 'B')
    {
        amount_of_read_and_displacements++;
        if (x == x->parent->left)
        {
            amount_of_read_and_displacements++;
            w = x->parent->right;
            if (w->color == 'R')
            {
                w->color = 'B';
                x->parent->color = 'R';
                left_rotate(x->parent);
                amount_of_read_and_displacements++;
                w = x->parent->right;
            }
            if (w->left->color == 'B' && w->right->color == 'B')
            {
                w->color = 'R';
                amount_of_read_and_displacements++;
                x = x->parent;
            }
            else
            {
                if (w->right->color == 'B')
                {
                    w->left->color = 'B';
                    w->color = 'R';
                    right_rotate(w);
                    amount_of_read_and_displacements++;
                    w = x->parent->right;
                }
                w->color = x->parent->color;
                x->parent->color = 'B';
                w->right->color = 'B';
                left_rotate(x->parent);
                amount_of_read_and_displacements++;
                x = root;
            }
        }
        else
        {   amount_of_read_and_displacements += 1;
            w = x->parent->left;
            
            if (w->color == 'R')
            {
                w->color = 'B';
                x->parent->color = 'R';
                right_rotate(x->parent);
                amount_of_read_and_displacements++;
                w = x->parent->left;
            }
            if (w->left->color == 'B' && w->right->color == 'B')
            {
                w->color = 'R';
                amount_of_read_and_displacements++;
                x = x->parent;
            }
            else
            {
                if (w->left->color == 'B')
                {
                    w->right->color = 'B';
                    w->color = 'R';
                    left_rotate(w);
                    amount_of_read_and_displacements++;
                    w = x->parent->left;
                }
                w->color = x->parent->color;
                x->parent->color = 'B';
                w->left->color = 'B';
                right_rotate(x->parent);
                amount_of_read_and_displacements++;
                x = root;
            }
        }
    }
    x->color = 'B';
}

void Red_black_tree::free_tree(Node* node)
{ 
    if (node == T_nil)
    { 
        return;
    } 
    free_tree(node->left);
    free_tree(node->right);

    printf("Deleting node: %d \n", node->key);
    free(node);
}

int Red_black_tree::height(){
    return height(root);
}

int Red_black_tree::height(Node* root){
    if (root == NULL) return 0;
    else if (root->left == T_nil && root->right == T_nil) return 1;
    else if (root->right == T_nil) return height(root->left) + 1;
    else if (root->left == T_nil)  return height(root->right) + 1;
    else                       return std::max(height(root->left), height(root->right)) + 1;

}

void Red_black_tree::print(){
    std::vector<int> road;
    print(root, 0, false, road);
}

void Red_black_tree::print(Node* root, int indent, bool left_tree, std::vector<int> road){
    if(root != NULL){
        if (root->left != T_nil){
            std::vector<int> left_road = road;
            left_road.push_back(-1);
            print(root->left, indent+1, true, left_road);
        }

        print_indent(indent, road);
        if (left_tree)
            std::cout << "/";
        if (!left_tree && indent != 0)
            std::cout << "\\";

        if(root->color == 'R'){
            std::cout << "\033[1;31m" << "-[" << root->key << "]" << "\033[0m" <<std::endl;
        }else{
             std::cout << "-[" << root->key << "]" <<std::endl;
        }


        if (root->right != T_nil){
            std::vector<int> right_road = road;
            right_road.push_back(1);
            print(root->right, indent+1, false, right_road);
        }
    }
}

void Red_black_tree::print_indent(int indent, std::vector<int> road){
    std::vector<char> output;
    int previous = 0;
    for(int i = road.size()-1; i >= 0; i--){
        if (previous == road[i] || previous == 0)
            output.push_back(' ');
        else {
            if (road[i] == 1 || road[i] == -1)
                output.push_back('|');
        }
        previous = road[i];
    }
    for(int i = output.size()-1; i >= 0; i--)
        std::cout << output.at(i);
}

int main(int argc, char** argv){
    int n;
    bool should_print = false;
    long long height = 0;
    long long max_height = 0;
    long long max_comparisons_diff = 0;
    long long max_displacements_diff = 0;
    std::cin >> n;
    int delete_arr[n];
    for (int i = 0; i < n ; i++){
        std::cin >> delete_arr[i];
    }

    Red_black_tree* tree = new Red_black_tree();
    T_nil = (Node*)malloc(sizeof(Node));
    T_nil->color = 'B';

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
        long long prev_comparisons = tree->get_amount_of_comparisons();
        long long prev_displacements = tree->get_amount_of_displacements();
        tree->insert_Node(source_arr[i]);
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

        tree->delete_Node(delete_arr[i]);

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