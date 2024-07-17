#include<iostream>

int main() {

    // testing some pointer stuff
    int* ptr = new int(42);
    std::cout << "the ptr points to a var whose value is: " << *ptr << "\n" <<
    "the ptr's r value is: " << ptr << "\n" <<
    "the ptr's own address is: " << &ptr 
    << std::endl;

    // the 'new' keyword means the var is allocated memory on the heap which is by def
    // dynamic. Using the *int we are making a pointer that points to that var on the 
    // heap 

    int* dynamicArr = new int[5];


}