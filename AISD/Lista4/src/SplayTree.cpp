#include <iostream>
#include <vector>
#include "SplayTree.h"

long long amount_of_comparisons=0;
long long amount_of_read_and_displacements=0;

long long SplayTree::get_amount_of_comparisons(){
    return amount_of_comparisons;
}

long long SplayTree::get_amount_of_displacements(){
    return amount_of_read_and_displacements;
}

void SplayTree::deleteNode(NodePtr node, int key) {
    amount_of_read_and_displacements++;
    NodePtr x = nullptr;
    NodePtr t, s;
    amount_of_read_and_displacements++;
    while (node != nullptr){
        amount_of_comparisons++;
        if (node->data == key) {
            amount_of_read_and_displacements++;
            x = node;
        }

        amount_of_comparisons++;
        if (node->data <= key) {
            amount_of_read_and_displacements++;
            node = node->right;
        } else {
            amount_of_comparisons++;
            amount_of_read_and_displacements++;
            node = node->left;
        }
        amount_of_read_and_displacements++;
    }

    amount_of_read_and_displacements++;
    if (x == nullptr) {
        std::cout<<"Couldn't find key in the tree"<<std::endl;
        return;
    }
    split(x, s, t); // Podziel drzewo
    amount_of_read_and_displacements++;
    if (s->left){ // Usuń x
        amount_of_read_and_displacements++;
        s->left->parent = nullptr;
    }
    root = join(s->left, t);
    delete(s);
    amount_of_read_and_displacements++;
    s = nullptr;
}

// Rotacja w lewo
void SplayTree::leftRotate(NodePtr x) {
    amount_of_read_and_displacements += 2;
    NodePtr y = x->right;
    x->right = y->left;

    amount_of_read_and_displacements++;
    if (y->left != nullptr) {
        amount_of_read_and_displacements++;
        y->left->parent = x;
    }
    amount_of_read_and_displacements += 2;
    y->parent = x->parent;
    if (x->parent == nullptr) {
        amount_of_read_and_displacements++;
        this->root = y;
    } else if (x == x->parent->left) {
        amount_of_read_and_displacements += 2;
        x->parent->left = y;
    } else {
        amount_of_read_and_displacements += 3;
        x->parent->right = y;
    }
    amount_of_read_and_displacements += 2;
    y->left = x;
    x->parent = y;
}

// Rotacja w prawo
void SplayTree::rightRotate(NodePtr x) {
    amount_of_read_and_displacements += 2;
    NodePtr y = x->left;
    x->left = y->right;

    amount_of_read_and_displacements++;
    if (y->right != nullptr) {
        amount_of_read_and_displacements++;
        y->right->parent = x;
    }
    amount_of_read_and_displacements += 2;
    y->parent = x->parent;
    if (x->parent == nullptr) {
        amount_of_read_and_displacements++;
        this->root = y;
    } else if (x == x->parent->right) {
        amount_of_read_and_displacements += 2;
        x->parent->right = y;
    } else {
        amount_of_read_and_displacements += 3;
        x->parent->left = y;
    }
    amount_of_read_and_displacements += 2;
    y->right = x;
    x->parent = y;
}

// Splaying
void SplayTree::splay(NodePtr x) {
    amount_of_read_and_displacements++;
    while (x->parent) {
        amount_of_read_and_displacements++;
        if (!x->parent->parent) {
            amount_of_read_and_displacements++;
            if (x == x->parent->left) {
                // Zig rotation
                rightRotate(x->parent);
            } else {
                amount_of_read_and_displacements++;
                // Zag rotation
                leftRotate(x->parent);
            }
        } else if (x == x->parent->left && x->parent == x->parent->parent->left) {
            amount_of_read_and_displacements += 2;
            // Zig-zig rotation
            rightRotate(x->parent->parent);
            rightRotate(x->parent);
        } else if (x == x->parent->right && x->parent == x->parent->parent->right) {
            amount_of_read_and_displacements += 4;
            // Zag-zag rotation
            leftRotate(x->parent->parent);
            leftRotate(x->parent);
        } else if (x == x->parent->right && x->parent == x->parent->parent->left) {
            amount_of_read_and_displacements += 6;
            // Zig-zag rotation
            leftRotate(x->parent);
            rightRotate(x->parent);
        } else {
            // Zag-zig rotation
            rightRotate(x->parent);
            leftRotate(x->parent);
        }
    }
}

// Połącz drzewa
NodePtr SplayTree::join(NodePtr s, NodePtr t){
    amount_of_read_and_displacements++;
    if (!s) {
        return t;
    }
    amount_of_read_and_displacements++;
    if (!t) {
        return s;
    }
    amount_of_read_and_displacements++;
    NodePtr x = maximum(s);
    splay(x);
    x->right = t;
    t->parent = x;
    amount_of_read_and_displacements += 2;
    return x;
}

// Podziel drzewo na 2 drzewa
void SplayTree::split(NodePtr &x, NodePtr &s, NodePtr &t) {
    splay(x);
    amount_of_read_and_displacements++;
    if (x->right) {
        amount_of_read_and_displacements += 2;
        t = x->right;
        t->parent = nullptr;
    } else {
        amount_of_read_and_displacements += 2;
        t = nullptr;
    }
    s = x;
    s->right = nullptr;
    x = nullptr;
    amount_of_read_and_displacements += 3;
} 


SplayTree::SplayTree() {
    root = nullptr;
}


// Znajdz maximum nodea
NodePtr SplayTree::maximum(NodePtr node) {
    while (node->right != nullptr) {
        node = node->right;
    }
    return node;
}

// Dodaj element do drzewa
void SplayTree::insert(int key) {
    // normal BST insert
    NodePtr node = new Node;
    node->parent = nullptr;
    node->left = nullptr;
    node->right = nullptr;
    node->data = key;
    NodePtr y = nullptr;
    NodePtr x = this->root;
    amount_of_read_and_displacements += 5;

    // Przechodzimy w dół drzewa, aż y (który będzie rodzicem nowego nodea) będzie nodem w ostatnim rzędzie drzewa
    amount_of_read_and_displacements++;
    while (x != nullptr) {
        y = x;
        amount_of_read_and_displacements++;
        amount_of_comparisons++;
        if (node->data < x->data) {
            x = x->left;
            amount_of_read_and_displacements++;
        } else {
            amount_of_comparisons++;
            amount_of_read_and_displacements++;;
            x = x->right;
        }
        amount_of_read_and_displacements++;
    }

    // Ustawiamy y jako rodzica nowego nodea
    node->parent = y;
    amount_of_read_and_displacements += 2;
    if (y == nullptr) {
        amount_of_read_and_displacements++;
        root = node;
    } else if (node->data < y->data) {
        amount_of_comparisons++;
        amount_of_read_and_displacements++;;
        y->left = node;
    } else {
        amount_of_comparisons += 2;;
        amount_of_read_and_displacements++;
        y->right = node;
    }

    // Splay
    splay(node);
}

// Usuń element z drzewa
void SplayTree::deleteNode(int data) {
    deleteNode(this->root, data);
}

int SplayTree::height(){
    return height(this->root);
}

int SplayTree::height(NodePtr root){
    if (root == nullptr) return 0;
    else if (root->left == nullptr && root->right == nullptr) return 1;
    else if (root->right == nullptr) return height(root->left) + 1;
    else if (root->left == nullptr)  return height(root->right) + 1;
    else                       return std::max(height(root->left), height(root->right)) + 1;

}

void SplayTree::print(){
    std::vector<int> road;
    print(this->root, 0, false, road);
}

void SplayTree::print(NodePtr root, int indent, bool left_tree, std::vector<int> road){
    if(root != nullptr){
        if (root->left != nullptr){
            std::vector<int> left_road = road;
            left_road.push_back(-1);
            print(root->left, indent+1, true, left_road);
        }

        print_indent(indent, road);
        if (left_tree)
            std::cout << "/-";
        if (!left_tree && indent != 0)
            std::cout << "\\-";
        
        std::cout << "[" << root->data << "]" << std::endl;
        


        if (root->right != nullptr){
            std::vector<int> right_road = road;
            right_road.push_back(1);
            print(root->right, indent+1, false, right_road);
        }
    }
}

void SplayTree::print_indent(int indent, std::vector<int> road){
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