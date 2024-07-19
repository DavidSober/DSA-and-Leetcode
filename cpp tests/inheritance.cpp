#include<iostream>


namespace car_name_space { // putting parent and child classes in name space

class vehicle {
    protected: // makes members available to derived classes
    std::string type;
    int speed;
    int fuel;

    protected: // means this can be inhereited 
    void test() {
        std::cout << "hello" << std::endl;
    }

};

class car: public vehicle {
    public:
    void testingI() {
        test();     // we can call the inherited function directly 
    }

};
} // car namespace


int main() {
    car_name_space::car obj;
    obj.testingI();
}