#include "Node.hpp"

Node::Node() : prev(nullptr), next(nullptr) {}
Node::Node(int val, Node* prev, Node* next) : prev(prev), next(next), val(val){}
Node::Node(int val) : prev(nullptr), next(nullptr), val(val) {}
