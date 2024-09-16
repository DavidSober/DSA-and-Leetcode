#include<iostream>


// pure virtual functions are similar to virtual functions 
// except they have no default implementation. You must 
// implement them in a child object. 
// they are C++'s version of interfaces


class Parent {
    public:
        virtual void lol() = 0;
};

class Child : public Parent {
    public:
        void lol() override {
            std::cout << "hello pure virtual world" << std::endl;
        }
};



int main() {

// since parent is an interface it is considered an abstract class
// thus we cannot make it into an object, this is because it has
// a pure virtual function 
// Parent* obj1 = new Parent(); 
Child* obj2 = new Child();
obj2->lol();


}