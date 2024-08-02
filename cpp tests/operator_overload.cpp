#include<iostream>

// we can take operators like +, -, ==, etc. and attatch their use to 
// members of same class objects. 

class Complex {
public:
    double real, imag;

    // here is a typical constructor
    Complex(double r, double i) : real(r), imag(i) {}

    // example of default constructor 
    Complex() : real(0), imag(0) {}

    // Operator overload ex of addition
    // make everything const to ensure no mods happen to objects
    Complex operator + (const Complex& other) const {
        // note that we are using our member vars real and other 
        // and addin them to an object of the same type. since it
        // is the same type we know its member vars for real and imag
        // will be compatible with addition 
        return Complex(real + other.real, imag + other.imag);
    }

    // Operator overload for == operator 
    // we have a return type bool whereas above it is just the object
    // this is because we make a c3 object below that has the result of the additon
    // above stored in its member vars. and we use the print function in this 
    // class to print those member vars. 
    bool operator == (const Complex& other) const {
        return (real == other.real && imag == other.imag);
    }

    // print the Complex number
    void print() const {
        std::cout << real << " + " << imag << "i" << std::endl;
    }

    // Operator overload that will only return a double and not an object
    double operator - (const Complex& other) const {
        return -real - other.real - imag - other.imag;
    }

};


int main() {
    Complex c1(1.0, 2.0);          // Calls parameterized constructor
    Complex c2(2.0, 3.0);          // Calls parameterized constructor
    Complex c3 = c1 + c2;          // Uses overloaded operator+
    Complex c4 = c3;               // Uses copy constructor

    c3.print(); // Outputs: 3.0 + 5.0i
    c4.print(); // Outputs: 3.0 + 5.0i

    if (c3 == c4) {                // Uses overloaded operator==
        std::cout << "c3 and c4 are equal" << std::endl;
    } else {
        std::cout << "c3 and c4 are not equal" << std::endl;
    }

    std::cout << c1 - c2 << std::endl;

    return 0;
}