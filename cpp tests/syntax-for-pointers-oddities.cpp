#include<iostream>




int main() {

    int xval = 10;
    int yval = 11;
    // so supposedly the syntax for pointers can be done in one of two ways
    // like this 
    int* x = &xval;
    // and this
    int *y = &yval;

    // here if we dereference the pointers we print the vals of 
    // x and y even though we used a different syntax for defining 
    // x and y pointers...
    // thus we are able to just choose which sytle we prefer.
    // that seems crazy considering all the other syntax requirements 
    // in cpp
    std::cout << *x << " " << *y << std::endl;


}