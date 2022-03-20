#ifndef FIFO_HPP
#define FIFO_HPP

#include "Node.hpp"

class Fifo {
private:
    Node* front = nullptr;
    Node* rear = nullptr;
    bool isEmpty();
public:
    Fifo();
    void push(int elem);
    int pop();
};

#endif