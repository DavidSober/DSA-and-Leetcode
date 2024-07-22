// main.cpp
#include <iostream>
#include "sub_dir/helper.cpp"
#include "sub_dir/helper_1.cpp"

int main() {
    math m;
    printing P;
    std::cout << "starting project" << std::endl;
    std::cout << "3 + 4 = " << m.add(3, 4) << std::endl;
    std::cout << "7 - 2 = " << m.sub(7, 2) << std::endl;
    std::cout << "6 * 5 = " << m.mult(6, 5) << std::endl;
    std::cout << "8 / 2 = " << m.div(8, 2) << std::endl;
    P.p1();
    P.p2();
    P.p3();
    
    return 0;
}
