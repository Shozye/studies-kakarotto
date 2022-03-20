#include "Lifo.hpp"
#include<iostream>
#include<exception>

Lifo::Lifo() : head(nullptr) {}

bool Lifo::isEmpty(){
    return head==nullptr;
}
void Lifo::push(int elem){
    this->head = new Node(elem, head);
}
int Lifo::pop(){
    if(this->isEmpty()){
        throw std::out_of_range("Stack empty");
    }
    auto head_ptr = head;
    int to_return = head->val;
    head = head -> next;
    delete head_ptr;
    return to_return;
}