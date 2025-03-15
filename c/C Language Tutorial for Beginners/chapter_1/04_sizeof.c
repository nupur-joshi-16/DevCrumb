#include <stdio.h>

int main() {
    int my_age = 41;
    float my_weight = 68.5;
    char my_char = 'I'; //I for Intelligent 😜

    printf("Size of my_age variable: %zu\n", sizeof(my_age));
    printf("Size of my_weight variable: %zu\n", sizeof(my_weight));
    printf("Size of my_char variable: %zu\n", sizeof(my_char));
    return 0;
}