// scratchpad 
#include<iostream>
#include<vector>
#include<tuple>
#include<unordered_map>

int main() {

    // std::cout << "hello" << std::endl;

    // std::vector<int> lst = {1,2,3,4,5};

    // for (int val: lst) {
    //     std::cout << val << std::endl;
    // }
    
    std::vector<int> lst = {1,1,3,4,5,2,1};
    std::unordered_map<int, int> F;

    for (auto& val : lst) {
        F[val]++;
    }
    for (auto& pair : F) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }

}