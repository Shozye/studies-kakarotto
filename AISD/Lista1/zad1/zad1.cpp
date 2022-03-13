#include"Fifo.hpp"
#include"Lifo.hpp"
#include<iostream>

void test_lifo(int AMOUNT_INSERT){
    Lifo* lifo = new Lifo();
    std::cout << "Start pushing to lifo: " << std::endl;
    for(int i=0; i< AMOUNT_INSERT; i++){
        lifo->push(i);
        std::cout<< i << " "; 
    }
    std::cout << "\nStart popping lifo: " << std::endl;
    for(int i=0; i<AMOUNT_INSERT; i++){
        std::cout << lifo -> pop() << " ";
    }
    std::cout << std::endl;
};
void test_fifo(int AMOUNT_INSERT){
    Fifo* fifo = new Fifo();
    std::cout << "Start pushing to fifo: " << std::endl;
    for(int i=0; i< AMOUNT_INSERT; i++){
        fifo->push(i);
        std::cout<< i << " "; 
    }
    std::cout << std::endl;
    std::cout << "Start popping fifo: " << std::endl;
    for(int i=0; i<AMOUNT_INSERT; i++){
        std::cout << fifo->pop() << " ";
    }
    std::cout << std::endl;
};


int main(){
    int AMOUNT_INSERT = 10;
    test_lifo(AMOUNT_INSERT);
    test_fifo(AMOUNT_INSERT);
}