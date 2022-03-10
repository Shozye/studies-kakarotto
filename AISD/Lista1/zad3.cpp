#include<iostream>
#include <stdlib.h>     
#include <time.h> 
#include <stdio.h>
#include<chrono>
#include <iomanip>

template<class T>
struct Node {
    T val;
    Node* prev = nullptr;
    Node* next = nullptr;
    Node(){}
    Node(T val, Node* prev, Node* next){
        this -> val = val;
        this -> prev = prev;
        this -> next = next;
    }
    Node(T val){
        this -> val = val;
    }
};
template<class T>
struct DoubleCyclicLinkedList{
    Node<T>* main = nullptr;
    int length;
    DoubleCyclicLinkedList(){} 
    void append(T elem){
        if (main == nullptr){
            main = new Node<T>(elem);
            main -> next = main;
            main -> prev = main;
        }
        else{
            Node<T>* last_node = main->prev;
            Node<T>* new_node = new Node<T>(elem, last_node, main);
            last_node -> next = new_node;
            main -> prev = new_node;           
        }
        length++;
    }
    T at(int index){
        if (this->isEmpty()){
            throw std::out_of_range("List empty");
        }
        if (index >= length){
            index %= length;
        }
        Node<T>* temp;
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
    bool isEmpty(){
        return main == nullptr;
    }
};

template<typename T> void printElement(T t)
{
    std::cout << std::setw(8) << t;
}

int main(){
    srand (time(NULL));
    DoubleCyclicLinkedList<int>* list = new DoubleCyclicLinkedList<int>();
    for(int i = 0; i < 1050; i++){
        list->append(i);
    }
    int time_array[12];
    int elem_index = 1;
    for(int i = 0; i < 12; i++){
        auto start = std::chrono::high_resolution_clock::now();
        for(int _=0; _<100000; _++){
            if(i == 11)
                elem_index = std::rand()%1000;
            list -> at(elem_index);
        }
        auto stop = std::chrono::high_resolution_clock::now();
        auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
        time_array[i] = duration.count();
        elem_index *= 2;
    }
    
    elem_index = 1;
    std::cout << "Tabela czasu[ms] wymaganego na dobranie sie 100 000 do elementu o indeksie INDEX" << std::endl;
    printElement("INDEX");
    for(int i = 0; i < 11; i++){
        printElement(elem_index);
        elem_index*=2;
    }
    printElement("RAND");
    std::cout<<std::endl;
    printElement("CZAS[ms]");
    for(int i = 0; i < 12; i++){
        printElement(time_array[i]);
    }
    std::cout<<std::endl;
}