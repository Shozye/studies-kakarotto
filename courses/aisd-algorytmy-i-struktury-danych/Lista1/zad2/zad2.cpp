#include <iostream>
#include <stdlib.h>
#include <time.h> 
#include <stdio.h>
#include <chrono>
#include <iomanip>

#include "LinkedList.hpp"

template <class T>
void printElement(T t)
{
    std::cout << std::setw(8) << t;
}
int main(){
    srand (time(NULL));
    LinkedList* list = new LinkedList();
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
    
    LinkedList* first_list = new LinkedList();
    LinkedList* second_list = new LinkedList();
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