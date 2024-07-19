#include <iostream>

struct Node {
    int value;
    Node* next;

    Node(int val) : value(val), next(nullptr) {}
};

class TestClass {
    int value1;
    int value2;
    int value3;
    public:
    TestClass() : value1(1), value2(2), value3(3) {

    }
    public:
    void print() {
        std::cout << value1 << value2 << value3 << std::endl;
    }
};

int main() {
    
    Node node(3);
    std::cout << "Node value is: " << node.value << std::endl;
    TestClass object;
    object.print();

    int arr[5] = {1,2,3,69,5};
    int i = 0;
    while(arr[i] != 69) {
        std::cout << "not 69" << std::endl;
        i++;
    }

}