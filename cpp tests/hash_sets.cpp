#include<iostream>
#include<unordered_set>

void print(std::unordered_set<int> hs) {
    std::cout << "elements in the hash set are: " << std::endl;
    for (const auto& element : hs) {
        std::cout << element << std::endl;
    }
}

void find_el_in_hmap(std::unordered_set<int> hs, int el) {
    // checking if an element exists in the set
    std::cout << "let us see if the num: " << el << " is in the hash set... " << std::endl;
    // we use the find function which will iterate over the hashset if it does not find 
    // the element in question it will return hs.end() hence the condition 
    if (hs.find(el) != hs.end()) {
        std::cout << "we found the element 3 in the hash set" << std::endl;
    } else {
        std::cout << "nope!" << std::endl;
    }
}

int main() {
    // declare it
    std::unordered_set<int> hash_set;
    hash_set.insert(1);
    hash_set.insert(2);
    hash_set.insert(3);
    hash_set.insert(4);

    print(hash_set);
    find_el_in_hmap(hash_set, 3);
    find_el_in_hmap(hash_set, 69);
    

}