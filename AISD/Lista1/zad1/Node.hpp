#ifndef NODE_HPP
#define NODE_HPP

struct Node{
    int val{};
    Node* next = nullptr;
    Node();
    explicit Node(int val);
    Node(int val, Node* next);
};

#endif