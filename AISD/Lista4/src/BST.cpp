#include<iostream>
#include"BST.h"
#include<vector>
#include <stdexcept>

int amount_of_comparisons=0;
int amount_of_read_and_displacements=0;

int BST::get_amount_of_comparisons(){
    return amount_of_comparisons;
}

int BST::get_amount_of_displacements(){
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

BST::BST(){
    left = nullptr;
    right = nullptr;
    empty = true;
}

BST::~BST() {
}

void BST::insert(int k){
    if (empty) {
        amount_of_read_and_displacements += 1;
        value = k;
        empty = false;
        return;
    }
    amount_of_comparisons++;
    if (k <= value) {
        if(left == nullptr)
            this->left = new BST();
        left->insert(k);
    }
    else{
        if(right == nullptr)
            right = new BST();
        right->insert(k);
    }
}
void BST::del(int k){
    if(empty){
        throw std::logic_error("Can't del from empty tree!");
    }
    amount_of_comparisons++;
    if(value == k){ // only possible in root node
        if (left == nullptr && right == nullptr){
            empty = true; 
            amount_of_read_and_displacements += 2;
        }
        else if (left == nullptr){
            BST* saved = this->right;
            value = saved->value;
            left = saved->left;
            right = saved->right;
            delete saved;
            amount_of_read_and_displacements+= 6;
        }
        else if(right == nullptr){
            BST* saved = this->left;
            value = saved->value;
            left = saved->left;
            right = saved->right;
            delete saved;
            amount_of_read_and_displacements+= 7;
        }
        else{
            int value_of_node_to_swap = right->leftmost();
            del(value_of_node_to_swap);
            this->value = value_of_node_to_swap;
            amount_of_read_and_displacements+= 5;
        }
    }
    amount_of_comparisons += 1;
    if (k < value){
        amount_of_read_and_displacements += 1;
        if (left != nullptr){
            amount_of_comparisons += 1;
            if (left->value == k){
                BST* saved = this->left;
                if(left -> left == nullptr && left->right == nullptr){
                    this->left = nullptr;
                    delete saved;
                    amount_of_read_and_displacements+= 3;
                }
                else if(left->left == nullptr){
                    this->left = saved->right;
                    delete saved;
                    amount_of_read_and_displacements+= 4;
                }
                else if(left->right == nullptr){
                    this->left = saved -> left;
                    delete saved;
                    amount_of_read_and_displacements+= 5;
                }
                else{
                    int value_of_node_to_swap = left->right->leftmost();
                    left->del(value_of_node_to_swap);
                    this->left->value = value_of_node_to_swap;
                    amount_of_read_and_displacements += 3;
                }
            }
            else{
                left->del(k);
            }
        }
    }
    else{
        amount_of_read_and_displacements += 1;
        if (right != nullptr){
            amount_of_comparisons += 1;
            if (right->value == k){
                BST* saved = this->right;
                if(right -> left == nullptr && right->right == nullptr){
                    this->right = nullptr;
                    delete saved;
                    amount_of_read_and_displacements += 3;
                }
                else if(right->left == nullptr){
                    this->right = saved->right;
                    delete saved;
                    amount_of_read_and_displacements += 4;
                }
                else if(right->right == nullptr){
                    this->right = saved -> left;
                    delete saved;
                    amount_of_read_and_displacements += 5;
                }
                else{
                    int value_of_node_to_swap = right->right->leftmost();
                    right->del(value_of_node_to_swap);
                    this->right->value = value_of_node_to_swap;
                    amount_of_read_and_displacements += 3;
                }
            }
            else{
                right->del(k);
            }
        } 
    }
}
int BST::height(){
    if (empty) return 0;
    else if (left == nullptr && right == nullptr) return 1;
    else if (right == nullptr) return left->height() + 1;
    else if (left == nullptr)  return right->height() + 1;
    else                       return std::max(left->height(), right->height()) + 1;

}

void BST::print(){
    std::vector<int> road;
    print(0, false, road);
}

void BST::print(int indent, bool left_tree, std::vector<int> road){
    if(!empty){
        if (left != nullptr){
            std::vector<int> left_road = road;
            left_road.push_back(-1);
            left->print(indent+1, true, left_road);
        }

        print_indent(indent, road);
        if (left_tree)
            std::cout << "/";
        if (!left_tree && indent != 0)
            std::cout << "\\";
        std::cout << "-[" << value << "]" << std::endl;


        if (right != nullptr){
            std::vector<int> right_road = road;
            right_road.push_back(1);
            right->print(indent+1, false, right_road);
        }
    }
}

void BST::inorder(){
    if(!empty){
        if (left != nullptr)
            left->inorder();
        else
            std::cout << "N";
        std::cout << value;
        if (right != nullptr)
            right->inorder();
        else
            std::cout << "N";
    }
}

int BST::leftmost(){
    if(empty){
        throw std::logic_error("Can't get leftmost from empty tree");
    }
    amount_of_read_and_displacements += 1;
    if (left == nullptr) return value;
    return left->leftmost();
}