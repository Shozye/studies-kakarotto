#include<iostream>
#include<exception>
template<class T>
struct Node{
    T val;
    Node* next = nullptr;
    Node(){};
    Node(T val){ this->val = val;}
    Node(T val, Node* next){
        this->val = val;
        this->next = next; 
    }
};
template<class T>
class Lifo{
private:
    Node<T>* head=nullptr;
    bool isEmpty(){
        if (head == nullptr)
            return true;
        return false;
    }
public:
    Lifo(){}
    ~Lifo(){ delete head; }
    void push(T elem){ 
        this->head = new Node<T>(elem, head);
    }
    T pop(){
        if(this->isEmpty()){
            throw std::out_of_range("Stack empty");
        }
        auto head_ptr = head;
        T to_return = head->val;
        head = head -> next;
        delete head_ptr;
        return to_return;
    }
};
template<class T>
class Fifo{
private:
    Node<T>* front = nullptr;
    Node<T>* rear = nullptr;
    bool isEmpty(){
        if (front==nullptr)
            return true;
        return false;
    }
public:
    void push(T elem){
        if (this->isEmpty()){
            front= new Node(elem);
            rear = front;
        }
        else{
            Node<T>* next_node = new Node(elem);
            rear->next = next_node;
            rear = rear->next;
        }
    }
    T pop(){
        if(this->isEmpty()){
            throw std::out_of_range("Stack empty");
        }
        Node<T>* saved_front = front;
        front = front->next;
        T to_return = saved_front->val;
        delete saved_front;
        return to_return;
    }
};

void test_lifo(int AMOUNT_INSERT){
    Lifo<int> lifo = Lifo<int>();
    std::cout << "Start pushing to lifo: " << std::endl;
    for(int i=0; i< AMOUNT_INSERT; i++){
        lifo.push(i);
        std::cout<< i << " "; 
    }
    std::cout << "\nStart popping lifo: " << std::endl;
    for(int i=0; i<AMOUNT_INSERT; i++){
        std::cout << lifo.pop() << " ";
    }
    std::cout << std::endl;
};
void test_fifo(int AMOUNT_INSERT){
    Fifo<int>* fifo = new Fifo<int>();
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
    int AMOUNT_INSERT = 100;
    test_lifo(AMOUNT_INSERT);
    test_fifo(AMOUNT_INSERT);
    
}