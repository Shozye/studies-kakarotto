#ifndef NODE_HPP
#define NODE_HPP

struct Node{
    int val;
    Node* next = nullptr;
    Node* prev = nullptr;
    Node();
    Node(int val);
    Node(int val, Node* next);
};

#endif