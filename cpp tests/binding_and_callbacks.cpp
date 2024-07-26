#include<iostream>
#include<functional>

// callbacks are when you pass a function as an arg into another function
// this allows the called function to execute the callback at a specific time.
// think of the Timer function in arduino that is an example of a callback

                                     // here we declare the callback in the arg
void addition_callback(int a, int b, std::function<void(int)> callback) {
    int result = a + b;
    callback(result); // we pass in the addition into the callback
}

// larger explanation of std::function
// std::function is a part of the C++ Standard Library provided in the <functional> header. 
// It is a general-purpose, polymorphic function wrapper that can store, copy, and invoke 
// any callable target (like functions, lambda expressions, bind expressions, or other 
// function objects) that is callable with a specified signature.

// here is the function that we will pass in as a callback
void printRes(int result) {
    std::cout << "result is: " << result << std::endl;
}


// std::bind
// lets you pre set args for a function and store that as a separate object

// here is a simple function we will later bind
void messsage_to_person(std::string& name, std::string& message) {
    std::cout << name << " my message to you is: " << message << std::endl;
}

int main() {
    addition_callback(2, 2, printRes); // passing in the callback as third arg

    // here we will bind the greet function
    auto insult_message = std::bind(messsage_to_person, "Leo", std::placeholders::_1);
    // now we have binded some args to the function

    //calling binded function
    insult_message("you are the best!");


}