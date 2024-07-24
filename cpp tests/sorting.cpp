#include<iostream>
#include<vector>
#include<algorithm>


int main() {

    std::vector<int> list = {10, 2, 5, 6};

    for (int i = 0; i < list.size(); i++) {
        std::cout << list[i] << std::endl;
    }

    std::sort(list.begin(), list.end());
    std::cout << " now we print the sorted vector \n" << std::endl;
    for (int i = 0; i < list.size(); i++) {
        std::cout << list[i] << std::endl;
    }
    std::cout << " now we sort the vector in reverse \n" << std::endl;
    std::sort(list.begin(), list.end(), std::greater<int>());
    for (int i = 0; i < list.size(); i++) {
        std::cout << list[i] << std::endl;
    }

    // now let us sort based on custom criteria
    // starting with a matrix
    std::cout << "\n now printing matrx \n" << std::endl;
    std::vector<std::vector<int>> matrix = {
        {10, 82},
        {10, 1},
        {10, 13},
        {10, 2},
    };
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            std::cout << matrix[i][j] << std::endl;
        }
    }

    // std::sort()

}