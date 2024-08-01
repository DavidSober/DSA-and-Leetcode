#include <iostream>

class MyClass {
private:
    int privateValue;

public:
    MyClass(int value) : privateValue(value) {}

    // here we make our friend function declaration
    // if we get rid of the friend keyword we will lose access 
    // to members when inside this function
    friend void printPrivateValue(const MyClass& obj);
};

// Friend function definition
void printPrivateValue(const MyClass& obj) {
    std::cout << "Private value: " << obj.privateValue << std::endl;
}

int main() {
    MyClass myObj(42);
    printPrivateValue(myObj);  // Friend function can access privateValue
    return 0;
}
