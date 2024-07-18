#include<iostream>
#include<vector>

void print_elements(std::vector<int> vector) {
    std::cout << "vector has the following elements: " << std::endl;
    for (int i = 0; i < vector.size(); i++) {
        std::cout << vector[i] << std::endl;
    }
    std::cout << "\n" << std::endl;
}

int main() {
    // first way to make a vector 
    // declare one
    std::vector<int> testVec;
    testVec.push_back(20);
    testVec.push_back(21);
    testVec.push_back(22);

    // print nums in vector
    std::cout << "here are all elements of the first vector \n " << std::endl;
    print_elements(testVec);    
    
    // change val of vector element
    testVec[0] = 69; 
    print_elements(testVec);

    testVec.push_back(420);
    print_elements(testVec);
    

}