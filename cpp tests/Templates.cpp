#include<iostream>

// templates used to make generic functions that work with all data types
// typename is a generic term for any type it is used only in templates


// ex of template return type 
template<typename T> 
T add(T a, T b) {
    return a + b;
}

// you can use auto keyword for the same result ofc. 
// but auto keyword has limitations we will see below
auto AutoAdd( auto a, auto b) {
    return a + b;
}

// you can make class templates
template<typename T>
class GenericVAL {
    private: 
    T value_;

    public:
    GenericVAL(T value) : value_(value) {}

    T getValue() {
        return value_;
    }
};

class VAL {
    private: 
    int value_;

    public:
    GenericVAL(int value) : value_(value) {}

    int getValue() {
        return value_;
    }
};

int main() {

    // adding two floats and two ints
    // std::cout << add(2.8348939849843983, 3.832989389824398) << 
    // " and " <<
    // add(2,2) << " and now we try auto " <<
    // AutoAdd(2,2) << " and " << AutoAdd(2.4343342, 7.3141243) <<
    // std::endl;

    // now we create the object of the template class
    GenericVAL<int>* obj1 = new GenericVAL<int>(69);
    VAL* obj1 = new VAL(60);
}