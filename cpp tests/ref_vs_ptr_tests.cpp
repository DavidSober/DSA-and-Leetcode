#include<iostream>

// pointers will print l values whereas references will print r values
// dereferencing is just getting the r value that a ptr points to 

int main() {
    // address of '&'
    int some_var = 10;
    // we need int* since this var is now a pointer to an address
    // note below is just a pointer example nothing more
    int* address_of_some_var = &some_var; 
    std::cout << address_of_some_var << "and " << some_var << std::endl; 

    // refernce varible with &
    int& alias = some_var;
    std::cout << "alias of somevar = 10: " << alias << 
    " should be the same as " << some_var << std::endl;

    // ALL pointers need an address of operator to get the address 
    // that they point to. makes sense
    int* ptr = &some_var; 
    std::cout << ptr << std::endl;

    // dereferencing is just getting the r value that a ptr points to
    int r_val = *ptr; // note you need to attatch the * to the ptr name still
    std::cout << " here is the r value of a pointer: " << r_val << std::endl;
}