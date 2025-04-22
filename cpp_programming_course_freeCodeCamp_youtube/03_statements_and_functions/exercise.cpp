#include <iostream>

int multiplyNumbers(int first_number, int second_number){
    int result = first_number * second_number;
    return result;
}

int main() {
    int multi = multiplyNumbers(10,3);
    std::cout << "Multiply : " << multi << std::endl;
    std::cout << "Multiply : " << multiplyNumbers(50, 30);
    return 0;
}

