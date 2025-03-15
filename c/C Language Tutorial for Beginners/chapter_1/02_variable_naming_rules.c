#include <stdio.h>

int main() {
    int nupur;       // Allowed
    int my_name;     // Allowed
    int _num;        // Allowed (starts with underscore)
    int name16;      // Allowed (number at the end is fine)

    // int nupur joshi;  // ❌ Not allowed (spaces not allowed)
    // int 16nupur;      // ❌ Not allowed (cannot start with a digit)
    // int @mail;        // ❌ Not allowed (special characters not allowed)
    // int return;       // ❌ Not allowed (reserved keyword)

    return 0;
}
