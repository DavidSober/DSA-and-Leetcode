#include<iostream>


class Base {
  public:
    // the virtual keyword here means we expect to override this 
    // function in a derived class
    // part of polymorphism 
    virtual void myFunction() { 
        std::cout << "hello" << std::endl;
     }

    void nonVirtualFunction() {
        std::cout << "not virtual" << std::endl;
    }
};




class Derived : public Base {
  public:
    // note we do not need the override keyword in the derived 
    // class to override the virtual function. HOWEVER YOU SHOULD USE IT regardless
    // here is why 
    // Override Purpose: It helps the compiler 
    // catch errors if the method does not actually override a base class 
    // method due to signature mismatches or if the base class method is not virtual.
    void myFunction() override { 
        std::cout << "world" << std::endl;
     }

    // we were able to hide a non virtual function.
    // here is how chat explains it
// To ensure that a method in a derived class overrides a base class method and 
// is part of polymorphism, the base class method must be marked as virtual. If 
// you omit virtual in the base class, the derived class method will simply hide 
// the base class method, not override it.
 
    void nonVirtualFunction() {
        std::cout << "huh" << std::endl;
    }
};

int main() {

    // Derived obj;
    // obj.myFunction();
    // obj.nonVirtualFunction();

// =========================================================================
    // so what happens if you do not override properly? 
    // you hide the base function but what does that mean? 
    // it means the following 
    // Behavior: The derived class method hides the base class method. 
    // This means that the method call depends on the type of the pointer 
    // or reference used to make the call, not the actual object type.

    Base* basePtr = new Derived();
    basePtr->nonVirtualFunction();
    // above will print the base implementation of the function
    // because its pointer is to the base class

    Derived* derivedPtr = new Derived();
    derivedPtr->nonVirtualFunction();  
    // similarly the derived will point to the derived function
    // bc the pointer points to the derived class
// =========================================================================

    // if we repeat the above on the correctly overrided virtual function
    // aka real polymorphism. we will see different behavior
    std::cout << "\n" << std::endl;

    // for both pointers below, when dereferencing the virtual function
    // we see the same result despite the pointers having different types (Base vs Derived)
    // both print "world" bc that is the derived override class 
    // the objects's function was actually overridden aka true polymorphism
    Base* basePtr2 = new Derived();
    basePtr2->myFunction();

    Derived* derivedPtr2 = new Derived();
    derivedPtr2->myFunction();  
}