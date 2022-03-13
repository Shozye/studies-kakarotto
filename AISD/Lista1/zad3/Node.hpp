#ifndef NODE_HPP
#define NODE_HPP

struct Node {
    int val;
    Node* prev;
    Node* next;
    Node();
    Node(int val, Node* prev, Node* next);
    Node(int val);
};

#endif