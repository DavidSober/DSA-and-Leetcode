#include<iostream>


// pointer to pointers and that syntax 
// test to see if it is actually required or recommended 

// you need to keep adding * as you increase the depth of pointers to pointers
// this does not scale well so just dont do it or use smart pointers

int main() {

    // first data
    int val = 10;

    int* ptr1 = &val;
    int** ptr2 = &ptr1; // pointer to another pointer

    std::cout << "here is pointer 1: " << " address " <<
    ptr1 << " val " << *ptr1 << " here is pointer 2: " <<
    " address " << ptr2 << " val " << *ptr2 << std::endl;


}