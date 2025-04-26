#include <iostream>

int main() {
    int favorite_number; // Variable declaration
    std::cout << "Enter your favorite number between 1 and 100: "; // User Input
    std::cin >> favorite_number;
    std::cout << "Amazing!! That's my favorite number too!" << std::endl;
    std::cout << "No really!!, " << favorite_number <<" is my favorite number!" << std::endl;
    return 0;
}