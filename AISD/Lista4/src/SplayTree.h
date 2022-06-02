#pragma once
#include <iostream>
#include <vector>

struct Node {
	int data;
	Node *parent;
	Node *left;
	Node *right;
};

typedef Node *NodePtr;

class SplayTree {
private:
	NodePtr root;
	void deleteNode(NodePtr node, int key);
	void leftRotate(NodePtr x);
	void rightRotate(NodePtr x);
	void splay(NodePtr x);
	NodePtr join(NodePtr s, NodePtr t);
	void split(NodePtr &x, NodePtr &s, NodePtr &t);
public:
	SplayTree();
	NodePtr maximum(NodePtr node);
	void insert(int key);
	NodePtr getRoot();
	void deleteNode(int data);
    int height();
    int height(NodePtr root);
    void print();
    void print(NodePtr root, int indent, bool left_tree, std::vector<int> road);
    void print_indent(int indent, std::vector<int> road);

    long long get_amount_of_comparisons();
    long long get_amount_of_displacements();
};