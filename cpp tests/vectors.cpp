#include<iostream>
#include<vector>

int main() {
    
    // declaring a vector
    std::vector<int> vec = {1, 2, 3};

    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << std::endl;
    }


}