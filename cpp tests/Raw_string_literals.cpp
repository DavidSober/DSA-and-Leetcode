#include<iostream>


// SUMMARY: we use raw string literals to avoid having special characters like 
// newline \n from affecting our string. that is all
// escape sequences are caused by special chars like // or /" things like that"

// starting with c strings. 
char str[] = "hello"; // in c strings are char arrays that end with \0
// creates a char array with the contents {'h', 'e', 'l', 'l', 'o', '\0'}.
// it is printed below

// now onto RAW string literals (only exist in cpp)
// syntax R"delimiter(content)delimiter", where delimiter can 
// be any sequence of characters. In your example, R"( ... )" uses
// parentheses () as delimiters.
char raw[] = 
    R"delimiterlol(hello world blah blah blah)delimiterlol";


int main() {
    // going through C string literal aka char array
    // for (auto el: str) {
    //     std::cout << el << std::endl;
    // }

    std::cout << raw << std::endl;

}