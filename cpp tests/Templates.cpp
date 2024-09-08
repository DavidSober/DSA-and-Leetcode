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
// essentially you can use them to take any data type for any number of vars
// in the class
template<typename T>
class GenericVAL {
    private: 
    T value_;
    T value_2_;

    public:
    GenericVAL(T value, T value2) : value_(value), value_2_(value2) {}

    T getValue() {
        return value_ + value_2_;
    }
};

// regular class here you need to specify the type unlike template
class VAL {
    private: 
    int value_;

    public:
    VAL(int value) : value_(value) {}

    int getValue() {
        return value_;
    }
};

// you can have many datatypes passed to a class template like this
template<class T, class U> 
class ManyTypeVAL {
    private:
        T val1_;
        U val2_;
    public:
        ManyTypeVAL(T val1, U val2) : val1_(val1), val2_(val2) {}

    void getVAL() {
        std::cout << "val1 is: " << val1_ << " val2 is " << val2_ << 
        " added together they are: " << val1_ + val2_ << std::endl;
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
    GenericVAL<int>* obj1 = new GenericVAL<int>(69, 'c'); // ascii c: 99
    VAL* obj2 = new VAL(60);

    auto genericVAL = obj1->getValue();
    std::cout << genericVAL << std::endl;
    
    // we define the multi type class template
    ManyTypeVAL<int, char>* obj3 = new ManyTypeVAL<int, char>(21, 'x');


    obj3->getVAL(); 
}