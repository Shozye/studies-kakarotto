#ifndef DOUBLE_CYCLIC_HPP
#define DOUBLE_CYCLIC_HPP

#include "Node.hpp"

struct DoubleCyclicLinkedList{
    Node* main;
    int length;
    DoubleCyclicLinkedList();
    void append(int elem);
    int at(int index);
    bool isEmpty();
    void merge_with(DoubleCyclicLinkedList* list2);
    void display();
};

#endif