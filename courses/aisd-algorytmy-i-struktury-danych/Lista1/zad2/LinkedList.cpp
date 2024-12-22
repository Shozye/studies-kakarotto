#include "LinkedList.hpp"
#include <iostream>
#include <stdlib.h>     
#include <time.h> 
#include <stdio.h>
#include <chrono>
#include <iomanip>

LinkedList::LinkedList() : head(nullptr) {}
void LinkedList::append(int elem){
    if (head == nullptr){
        head = new Node(elem);
    }
    else{
        auto temp = head;
        while (temp->next != nullptr){
            temp = temp->next;
        }
        temp->next = new Node(elem);
    }
}
int LinkedList::at(int index){
    auto temp = head;
    while (index != 0){
        if (temp == nullptr){
            throw std::out_of_range("Out of range");
        }
        temp = temp-> next;
        index--;
    }
    return temp->val;
}
void LinkedList::print_list(){
    auto temp = head;
    std::cout << "Printing list: " << std::endl;
    while(temp != nullptr){
        std::cout << temp->val << " ";
        temp = temp->next;
    }
    std::cout << std::endl;
}
void LinkedList::merge_with(LinkedList* list2){
    if (head == nullptr){
        head = list2->head;
        return;
    }
    auto temp = head;
    while(temp->next != nullptr){
        temp = temp->next;
    }
    temp->next = list2->head;
}