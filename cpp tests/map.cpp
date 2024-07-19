#include<iostream>
#include<map>

int main() {
    std::map<int, std::string> test_map = {
        // maps are ordered by default so its the same as a sortedmap in py
        {10000, "ok"},
        {1, "helo"},
        {233, "world"},
        {69, "helo"},
        {20, "lol"},
    };

    for (const auto& pair : test_map) {
        std::cout << pair.first << " " << pair.second << std::endl;
    }   

}