#include<iostream>

// step 1: declare private member vars for encapsulation
// step 2: use constructor to init member vars
// in object creation pass in values that will be assigned 
// to member vars.

class MATH {
private:
    // here we will declare our private member vars this is 
    // good practice for encapsulation, we do need to declare
    // them before assignemnt 
    int num_10_;
    int num_2_;
    std::string str_;

    // we will make a constructor to initialize member vars
    // when an object is created
public:
    MATH(int num_10, int num_2, std::string str) 
     : num_10_(num_10), num_2_(num_2), str_(str) {}

    void print_members() {
        std::cout << "printing member vars: \n"
        "num_10_ : " << num_10_ <<
        "\n num_2_ : " << num_2_ << "\n str_ : " << str_
        << std::endl;
    }
};


int main() {
    int x = 10;
    int y = 11;
    std::string test_str= "test";
    MATH test(x, y, test_str);
    // here is the dot operator showing how you can access member functions 
    // directly 
    test.print_members();

    // arrow operator derefernces a pointer to an object
    // so first we will make a pointer to the object test
    MATH* pointer = &test;

    // now we will dereference the pointer 
    // dereference means getting the r value
    // in this case that is activating the function
    pointer->print_members();
    
    // so when would you use this arrow operator? 
    // A: when you are creating objects on the heap
    // anytime you create anything on the heap you are working with
    // pointers and thus to access members of an object on the heap
    // you must dereference the object with the arrow
    // for example
    MATH* obj = new MATH(x, y, test_str); // new keyword means on heap

    // obj is now a pointer to the object of type MATH on the heap

    obj->print_members();

}