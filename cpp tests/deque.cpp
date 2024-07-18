#include<iostream>
#include<deque>
#include<vector>


int main() {
    // defining a deque here
    std::deque<int> deck_lol = {1, 2, 3, 4};

    // operations below
    // here is how you can see the front 
    std::cout << "here is the front" << deck_lol.front() << std::endl; // prints front or "bottom"
    std::cout << "here is the back" << deck_lol.back() << std::endl; // prints back or "top"

    // iterating over a deque is similar to iterating over a hash set 
    for (const int& element : deck_lol) {
        std::cout << element << std::endl;
    }   

    // pushing el to front
    deck_lol.push_front(27);

    // pushing el to back
    deck_lol.push_back(33);

    std::cout << "first el in deque " << deck_lol[0] << std::endl;

    // there are also pop_front() and pop_back() functions 

    // this type of for loop is called ranged based 
    // it is similar to the for num in nums: for loop in python
    int arr[3] = {10,20,30}; // make a static arr
    for (const int& el : arr) {
        std::cout << el << std::endl;
    }

    // now try a static matrix
    int matrix[3][3] = {{1,2,3}, {4,5,6}, {7,8,9}}; // ez matrix
    for (int i = 0; i < 3; i++) {           // ez loop through all elements pretty straightforward
        for (int j = 0; j < 3; j++) {
            std::cout << matrix[i][j] << std::endl;
        }
    }

    // now do the same but with a vector
    // same logic as with static array
    std::vector<int> myvect = {1,2,3}; // normal vector

    std::vector<std::vector<int>> vecMatrix = {{1,2,3}, {4,5,6}, {7,8,9}};
    for (int i = 0; i < 3; i++) {           
        for (int j = 0; j < 3; j++) {
            std::cout << vecMatrix[i][j] << std::endl;
        }
    }


}