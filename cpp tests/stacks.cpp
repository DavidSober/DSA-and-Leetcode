#include<iostream>
#include<stack>
#include<vector>

int main() {

    // std::stack<int> stack = {1,2,3,4}; // this does not work you need to do the below
    // first make vector
    std::vector<int> vec = {1,2,3,4,5};
    // now you convert your vector into a stack
    std::stack<int, std::vector<int>> stack(vec);

    // we cannot access elements freely in a stack in cpp we can only see the top
    // element 
    std::cout << "top of stack is " << stack.top() << std::endl;
    stack.push(69);
    std::cout << "we just pushed 69 so new top is " << stack.top() << std::endl;

    // note if you want to pop and store that val in an el you need to do 2 steps
    int num = stack.top();
    stack.pop();
    std::cout << "popped an el from stack and it is: " << num << std::endl;  
} 