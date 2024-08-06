#include<iostream>
#include<vector>
#include<unordered_map>
#include<algorithm>

std::vector<int> lst = {1,2,1,1,4,5,5,5,5,5,5};



int main() {
    // for (int i = 0; i < lst.size(); i++) {
    //     // first we print the lst
    //     std::cout << lst[i] << std::endl;
    // }

    std::unordered_map<int, int> F;

    for (int i = 0; i < lst.size(); i++) {
        // add the nums to the freq map
        F[lst[i]]++; // this is how you increment and add a key
        // similar to py really.
    }

    // how to iterate through unordered maps
    // the auto data type is also pass by reference
    for (auto& pair : F) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    // now we need to sort based off the freq hash map
    // sorting in cpp is only in place 
    // we pass a and b as ints by reference they are elements in the vector
    // whenever you sort and pass a lambda function your args in lambda are 
    // assumed to be part of the container you are sorting.
    // note the syntax to capture the freq map F is unique
    // we use ints a and b from vector to pass into F 
    std::sort(lst.begin(), lst.end(), [&F] (int& a, int& b) {
        return F[a] > F[b];
    });
    std::cout << "now printing sorted list" << std::endl;
    for (auto& item : lst) {
        std::cout << item << std::endl;
    }

}