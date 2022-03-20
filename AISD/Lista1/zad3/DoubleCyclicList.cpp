#include <iostream>
#include <stdlib.h>     
#include <time.h> 
#include <stdio.h>
#include <chrono>
#include <iomanip>

#include "DoubleCyclicList.hpp"

DoubleCyclicLinkedList::DoubleCyclicLinkedList() : length(0), main(nullptr) {}
void DoubleCyclicLinkedList::append(int elem){
    if (isEmpty()){
        main = new Node(elem);
        main -> next = main;
        main -> prev = main;
    }
    else{
        Node* last_node = main->prev;
        Node* new_node = new Node(elem, last_node, main);
        last_node -> next = new_node;
        main -> prev = new_node;           
    }
    length++;
}
int DoubleCyclicLinkedList::at(int index){
    if (this->isEmpty()){
        throw std::out_of_range("List empty");
    }
    if (index >= length){
        index %= length;
    }
    Node* temp;
    if(index > length/2){
        int counter = length-1;
        temp = main->prev;
        while (counter != index){
            counter--;
            temp=temp->prev;
        }
    }
    else{
        int counter = 0;
        temp = main;
        while(counter != index){
            counter++;
            temp=temp->next;
        }
    }
    return temp->val;
}

bool DoubleCyclicLinkedList::isEmpty(){
    return main==nullptr;
}

void DoubleCyclicLinkedList::merge_with(DoubleCyclicLinkedList* list2){
    if (main == nullptr){
        main = list2->main;
        return;
    }
    if (list2 -> main == nullptr){
        return;
    }
    Node* list2first = list2->main;
    Node* list2last = list2first->prev;
    Node* first = main;
    Node* last = main->prev;
    first->prev = list2last;
    list2last->next = first;
    last -> next = list2first;
    list2first -> prev = last;
    
}

void DoubleCyclicLinkedList::display(){
    if (!isEmpty()){
        std::cout << main->val << " ";
        Node* temp = main->next;
        while (temp != main){
            std::cout << temp->val << " ";
            temp = temp->next;
        }
        std::cout << ". . . " << std::endl;
    }
}