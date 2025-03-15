// Write a program to calculate simple interest for a set of values representing principal, number of years, and rate of interest.

// Process
// 01. Take user input for the principal amount
// 02. Take user input for the number of years
// 03. Take user input for the rate of interest
// 04. Calculate Simple Interest using the formula: (Principal * Rate of Interest * Number of Years) / 100
// 05. Calculate End Balance using the formula: Principal Amount + Simple Interest

#include <stdio.h>

int main() {
    printf("------------------------------------------------------------\n");
    printf("Simple Interest Calculator\n");
    printf("------------------------------------------------------------\n");

    float principal, interest_rate, term_years;

    // Taking input from the user
    printf("Please enter the Principal Amount: $");
    scanf("%f", &principal);
    printf("Please enter the Interest Rate (per year, in percentage): ");
    scanf("%f", &interest_rate);
    printf("Please enter the Term (in years): ");
    scanf("%f", &term_years);

    printf("------------------------------------------------------------\n");

    // Displaying input values
    printf("-- Principal Amount: \t$%.2f\n", principal);
    printf("-- Interest Rate: \t%.2f%%\n", interest_rate);
    printf("-- Term (years): \t%.2f\n", term_years);

    printf("------------------------------------------------------------\n");

    // Formula for simple interest calculation
    float total_interest = (principal * interest_rate * term_years) / 100;
    printf("-- Total Interest: \t$%.2f\n", total_interest);

    // Calculating end balance
    float end_balance = principal + total_interest;
    printf("-- End Balance: \t$%.2f\n", end_balance);

    printf("------------------------------------------------------------\n");

    return 0;
}
