#include<iostream>
#include"BST.h"
#include<vector>
#include <stdexcept>

using namespace std;

node* BST::makeEmpty(node* t) {
    amount_of_read_and_displacements++;
    if(t == NULL)
        return NULL;
    {
        makeEmpty(t->left);
        makeEmpty(t->right);
        delete t;
    }
    return NULL;
}

node* BST::insert(int x, node* t)
{
    amount_of_read_and_displacements+=1;
    if(t == NULL)
    {
        t = new node;
        t->data = x;
        t->left = t->right = NULL;
    }
    else if(x < t->data){
        amount_of_comparisons+=1;
        t->left = insert(x, t->left);
    }
    else if(x > t->data){
        amount_of_comparisons += 2;
        t->right = insert(x, t->right);
    }
    return t;
}

node* BST::findMin(node* t)
{
    if(t == NULL){
        amount_of_read_and_displacements+=1;
        return NULL;
    }
    else if(t->left == NULL){
        amount_of_read_and_displacements+=2;
        return t;
    }
    else{
        amount_of_read_and_displacements+=2;
        return findMin(t->left);
    }
}

node* BST::remove(int x, node* t) {
    node* temp;
    amount_of_read_and_displacements+=1;
    if(t == NULL)
        return NULL;
    else if(x < t->data){
        amount_of_comparisons += 1;
        t->left = remove(x, t->left);
    }
    else if(x > t->data){
        amount_of_comparisons += 2;
        t->right = remove(x, t->right);
    }
    else if(t->left && t->right)
    {
        amount_of_comparisons += 4;
        temp = findMin(t->right);
        t->data = temp->data;
        t->right = remove(t->data, t->right);
    }
    else
    {
        amount_of_comparisons +=4;
        amount_of_read_and_displacements += 2;
        temp = t;

        if(t->left == NULL)
            t = t->right;
        else if(t->right == NULL)
            t = t->left;
        delete temp;
    }

    return t;
}

BST::BST() {
    root = NULL;
}

BST::~BST() {
    root = makeEmpty(root);
}

void BST::insert(int x) {
    root = insert(x, root);
}

void BST::remove(int x) {
    root = remove(x, root);
}

long long BST::get_amount_of_comparisons(){
    return amount_of_comparisons;
}

long long BST::get_amount_of_displacements(){
    return amount_of_read_and_displacements;
}

void print_indent(int indent, std::vector<int> road){
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

int BST::height(){
    return height(root);
}
int BST::height(node* t){
    if (t == NULL) return 0;
    else if (t->left == NULL && t->right == NULL) return 1;
    else if (t->right == NULL) return height(t->left) + 1;
    else if (t->left == NULL)  return height(t->right) + 1;
    else                       return std::max(height(t->left), height(t->right)) + 1;
}

void BST::print(){
    std::vector<int> road;
    print(root, 0, false, road);
}

void BST::print(node* t, int indent, bool left_tree, std::vector<int> road){
    if(t != NULL){
        if (t->left != NULL){
            std::vector<int> left_road = road;
            left_road.push_back(-1);
            print(t->left, indent+1, true, left_road);
        }

        print_indent(indent, road);
        if (left_tree)
            std::cout << "/";
        if (!left_tree && indent != 0)
            std::cout << "\\";
        std::cout << "-[" << t->data << "]" << std::endl;


        if (t->right != NULL){
            std::vector<int> right_road = road;
            right_road.push_back(1);
            print(t->right, indent+1, false, right_road);
        }
    }
}
