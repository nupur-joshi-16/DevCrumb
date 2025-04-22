#include <iostream>
#include <string>

int main() {
    //std::cerr << "Error message : Something is wrong" << std::endl;
    //std::clog << "Log message : Something happened" << std::endl;

    // int age;
    // std::string name;

    // std::cout << "Please type your name and age : " << std::endl;
    // std::cin >> name;
    // std::cin >> age;

    // std::cout << "Hello " << name << ", You are " << age << " years old!" << std::endl;

    // Data with spaces

    std::string full_name;
    int user_age;

    std::cout << "Please type in your full name: ";
    std::getline(std::cin, full_name);

    std::cout << "Please type in your age: ";
    std::cin >> user_age;

    std::cout << "Hello " << full_name << ", You are " << user_age << " years old!" << std::endl;

    return 0;
}
