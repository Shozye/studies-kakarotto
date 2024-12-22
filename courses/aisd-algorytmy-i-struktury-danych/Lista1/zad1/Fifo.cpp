#include "Fifo.hpp"
#include<iostream>
#include<exception>

Fifo::Fifo() : front(nullptr) {}

bool Fifo::isEmpty(){
    return front==nullptr;
}

void Fifo::push(int elem){
    if (this->isEmpty()){
        front= new Node(elem);
        rear = front;
    }
    else{
        Node* next_node = new Node(elem);
        rear->next = next_node;
        rear = rear->next;
    }
}
int Fifo::pop(){
    if(this->isEmpty()){
        throw std::out_of_range("Stack empty");
    }
    Node* saved_front = front;
    front = front->next;
    int to_return = saved_front->val;
    delete saved_front;
    return to_return;
}
