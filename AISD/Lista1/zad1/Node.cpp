#include "Node.hpp"

Node::Node()= default;
Node::Node(int val) : val(val){}
Node::Node(int val, Node* next) : val(val), next(next) {}
