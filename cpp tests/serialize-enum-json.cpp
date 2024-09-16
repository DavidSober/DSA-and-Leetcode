#include<iostream>

// cannot import this until package manager like cmake and conan are configured 
// #include <nlohmann/json.hpp>

// first we get our enum

enum class List {
    kOne = 1,
    kTwo = 2,
    kThree = 3,
}; 


int main() {

    std::cout << "we will serialize the enum" << std::endl;

    
}