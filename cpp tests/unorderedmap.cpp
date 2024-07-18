#include<iostream>
#include<unordered_map>


int main() {
    // this is one way to make a hashmap one element at a time
    std::unordered_map<std::string, int> hashmap;
    hashmap["test1"] = 1;
    hashmap["test2"] = 2;
    hashmap["test3"] = 3;
    hashmap["whatasfdlkj"] = 69;

    // or just all at once
    std::unordered_map<std::string, int> HASHmap = {
        {"someone", 2},
        {"once told me", 3},
        {"that i wasnt", 3},
        {"the sharpest tool", 3},
        {"in the shead", 44444},
        {"but they dont stop commin", 3454},
    };

    // here is the long way to iterate through a hashmap
    // pass by reference and cannot chaneg elements
    for (std::pair<const std::string, int>& pair : HASHmap) {
        std::cout << "Key: " << pair.first << ", Value: " << pair.second << std::endl;
    }

    // we are passing by reference here and we are not allowed to change the reference elements
    std::cout << " now we will print using the faster way \n" << std::endl;
    for (const auto& pair: HASHmap) {
        std::cout << pair.first << " => " << pair.second << std::endl;
    }

    // we are passing by copy here and we can modify the copy
    std::cout << " now we will print without pass by reference \n" << std::endl;
    for (auto pair: HASHmap) {
        std::cout << pair.first << " => " << pair.second << std::endl;
    }

}