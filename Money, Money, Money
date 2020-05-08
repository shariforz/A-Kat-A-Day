// Money, Money, Money
// Level: 7kyu
/*
Mr. Scrooge has a sum of money 'P' that wants to invest, and he wants to know how many years 'Y' this sum has to be kept in the bank in order for this sum of money to amount to 'D'.
The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly, and the new sum is re-invested yearly after paying tax 'T'
Note that the principal is not taxed but only the year's accrued interest

http://www.codewars.com/kata/563f037412e5ada593000114/train/python

*/

def calculate_years(principal, interest, tax, desired):
    if principal >= desired:
        return 0
    result = principal * interest * (1 - tax) + principal
    return 1 if result >= desired else 1 + calculate_years(result, interest, tax, desired)

