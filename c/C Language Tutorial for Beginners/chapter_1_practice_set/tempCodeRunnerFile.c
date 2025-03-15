// Write a program to calculate simple interest for a set of values representing principal, number of years, and rate of interest.

// Process
// 01. Take user input for the principal amount
// 02. Take user input for the number of years
// 03. Take user input for the rate of interest
// 04. Calculate Simple Interest using the formula: (Principal * Rate of Interest * Number of Years) / 100
// 05. Calculate End Balance using the formula: Principal Amount + Simple Interest

#include<stdio.h>

int main(){
    printf("--------------------------------------------------\n");
    printf("Simple Interest Calculator\n");
    printf("--------------------------------------------------\n");

    int principal, interest_rate, term_years;

    // Taking input from the user
    printf("Please Enter Principal Amount: $");
    scanf("%d", &principal);
    printf("Please Enter Interest Rate (per year): ");
    scanf("%d", &interest_rate);
    printf("Please Enter Term (in years): ");
    scanf("%d", &term_years);

    printf("--------------------------------------------------\n");

    // Displaying input values
    printf("-- Principal Amount: \t$%d\n", principal);
    printf("-- Interest Rate: \t%d%%\n", interest_rate);
    printf("-- Term (years): \t%d\n", term_years);

    printf("--------------------------------------------------\n");

    // Formula for simple interest calculation
    int total_interest = (principal * interest_rate * term_years) / 100; 
    printf("-- Total Interest: \t$%d\n", total_interest);

    // Calculating end balance
    int end_balance = principal + total_interest;
    printf("-- End Balance: \t$%d\n", end_balance);

    printf("--------------------------------------------------\n");

    return 0;
}
