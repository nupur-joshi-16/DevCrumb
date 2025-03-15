#include <stdio.h>

int main() {
    printf("Enter your age: \n"); // Added \n for better formatting
    int age;
    scanf("%d", &age);
    // %d for Integer
    // %f for float
    // %c for char
    printf("User age: %d\n", age);
    return 0;
}
