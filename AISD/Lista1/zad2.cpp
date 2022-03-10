#include<iostream>
#include <stdlib.h>     
#include <time.h> 
#include <stdio.h>
#include<chrono>
#include <iomanip>

template<class T>
struct Node {
    T val;
    Node* next = nullptr;
    Node(){};
    Node(T val){this->val = val;}
};
template<class T>
struct LinkedList {
    Node<T>* head = nullptr;
    LinkedList(){};
    void append(T elem){
        if (head == nullptr){
            head = new Node<T>(elem);
        }
        else{
            auto temp = head;
            while (temp->next != nullptr){
                temp = temp->next;
            }
            temp->next = new Node<T>(elem);
        }
    };
    
    T at(int index){
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
    void print_list(){
        auto temp = head;
        std::cout << "Printing list: " << std::endl;
        while(temp != nullptr){
            std::cout << temp->val << " ";
            temp = temp->next;
        }
        std::cout << std::endl;
    }
    void merge_with(LinkedList* list2){
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
};

template<typename T> void printElement(T t)
{
    std::cout << std::setw(8) << t;
}

int main(){
    srand (time(NULL));
    LinkedList<int>* list = new LinkedList<int>();
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
    
    LinkedList<int>* first_list = new LinkedList<int>();
    LinkedList<int>* second_list = new LinkedList<int>();
    for(int i = 0; i < 10; i++){
        first_list->append(i);
        second_list->append(i+10);
    }
    std::cout<<"FIRST"<<std::endl;
    first_list->print_list();
    std::cout<<"SECOND"<<std::endl;
    second_list->print_list();
    first_list->merge_with(second_list);
    std::cout<<"FIRST_MERGED"<<std::endl;
    first_list->print_list();
    
    
}
