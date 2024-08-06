#include<iostream>
#include<vector>
#include<algorithm>
#include<tuple>

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

    // sorting a matrix based of custom criteria

    // we will sort based off the second element only
    std::sort(matrix.begin(), matrix.end(), [](std::vector<int> a, std::vector<int> b){
        return a[1] < b[1]; 
    }); 
    std::cout << "\n now we will print the sorted matrix \n" << std::endl;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[0].size(); j++) {
            std::cout << matrix[i][j] << std::endl;
        }
    }

    // now we will sort based on a heirarchy of criteria
    // first we will make a new matrix containing tuples
    std::vector<std::tuple<int, std::string>> newMatrix = {
        std::tuple<int, std::string>(90, "hello"),
        std::tuple<int, std::string>(2, "zz"),
        std::tuple<int, std::string>(6, "huh"),
        std::tuple<int, std::string>(2, "ok"),
    };
    std::cout <<"\nwe print a new matrix \n" << std::endl;
    // this is how you print for tuples
    // note that we are iterating through the vector and each element is a tuple called tup
    // we then print the first and second element of each tuple as we iterate 
    for (const auto& tup: newMatrix) {
        std::cout << std::get<0>(tup) << " " << std::get<1>(tup) << std::endl;
    }
    std::cout << "\nnow we sort this new matrix based of a heirarchy of criteria \n" << std::endl;
    // we sort here
    // note we use & to pass by reference, if we do not do this we will pass by copy by default and this will create more overhead
    // also we use const, to prevent the lambda function from modding the matrix. even if you will not mod the matrix in the lambda
    // it is there for documentation so that someone in the future will know the matrix should not change in the lambda...
    std::sort(newMatrix.begin(), newMatrix.end(), [](const std::tuple<int, std::string>& a, const std::tuple<int, std::string>& b) {
        if (std::get<0>(a) == std::get<0>(b)) {
            return std::get<1>(a) < std::get<1>(b);
        }
        return std::get<0>(a) < std::get<0>(b);

    });

    std::cout << "\nnow we print the now sorted matrix \n" << std::endl;
    for (const auto& tup: newMatrix) {
        std::cout << std::get<0>(tup) << " " << std::get<1>(tup) << std::endl;
    }

}