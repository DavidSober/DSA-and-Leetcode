#include<iostream>

int add(int x, int y) {
    return x + y;
}

float addF( float x, float y ) {
    return x + y;
}

int main() {
    char choice;
    std::cout << "enter a char any char";
    std::cin >> choice;

    switch (choice) {
        case 'a':
            std::cout << " you chose a " << std::endl;
            break;
        case 'b':
            std::cout << " you chose b " << std::endl;
            break;
        case 'c':
            std::cout << " you chose c " << std::endl;
            break;
        case 'd':
            std::cout << " you chose d " << std::endl;        
            break;
        case 'e':
            std::cout << " you chose e " << std::endl;
            break;
        case 'f':
            std::cout << add(1,2) << std::endl;
            break;
        case 'g': {
            // now we will ask them for two ints and we will convert the string into ints 
            // then add them and retur them as strings. super easy to to in python...
            char num1;
            char num2;
            std::cout << "enter a first num to add";
            std::cin >> num1;
            std::cout << "enter a second num to add";
            std::cin >> num2;
            int num1_I = num1 - '0'; // casting here you need to subtract 0 to convert the ascii
            int num2_I = num2 - '0';
            int result = add(num1_I, num2_I);
            std::cout << "here is " << num1 << " + " << num2 << ": " << result << std::endl;

            break; }
        case 'h': {
            // now try floats
            char num3;
            char num4;
            std::cout << "enter a first float to add";
            std::cin >> num3;
            std::cout << "enter a second float to add";
            std::cin >> num4;
            float num1_F = static_cast<float>(num3 - '0'); // casting here you need to subtract 0 to convert the ascii
            float num2_F = static_cast<float>(num4 - '0');
            float result_F = addF(num1_F, num2_F);
            std::cout << "here is " << num1_F << " + " << num2_F << ": " << result_F << std::endl;

            break; }
    }

}