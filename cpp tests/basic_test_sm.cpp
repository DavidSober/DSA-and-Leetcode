#include<iostream>

enum class State: uint8_t {
    kWaitingToStart = 1,
    kInit = 2,
    kIdle = 3,
    kFirstTask = 4,
    kSecondTask = 5,
};

bool kContinue_state_machine = false;
State state;

void processStateMachine() {
    
    switch (state)
    {
    case State::kWaitingToStart:
        std::cout << "waiting to start" << std::endl;
        if (kContinue_state_machine) {
            kContinue_state_machine = false;
            state = State::kInit
        }
        break;

    case State::kInit:
        std::cout << "in idle" << std::endl;
        if (kContinue_state_machine) {
            kContinue_state_machine = false;
            state = State::kWaitingToStart
        }
        break;
    default:
        break;
    }
}

bool handleCommand(char command) {
    if (command == 'a') {
        std::cout << "continue request receieved" << std::endl;
        kContinue_state_machine = true;
        return true;
    }

}


int main() {

    while (true)
    {
        char userInput;
        processStateMachine();
        std::cout << "enter a char ";
        std::cin >> userInput;
        handleCommand(userInput);
    }
    


}