#ifndef LINKED_LIST_HPP
#define LINKED_LIST_HPP

#include "Node.hpp"

struct LinkedList {
    Node* head;
    LinkedList();
    void append(int elem);
    int at(int index);
    void print_list();
    void merge_with(LinkedList* list2);
};

#endif