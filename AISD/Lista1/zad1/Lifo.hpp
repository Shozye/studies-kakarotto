#ifndef LIFO_HPP
#define LIFO_HPP

#include "Node.hpp"
class Lifo {
private:
    Node* head=nullptr;
    bool isEmpty();
public: 
    Lifo();
    void push(int elem);
    int pop();
};

#endif