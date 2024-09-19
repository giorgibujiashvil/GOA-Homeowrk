"""homework is codewars"""
"""task 1) Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered."""

import re

def increment_string(strng):
    # Regular expression to match the trailing number and capture the number and leading zeros
    match = re.search(r'(\d*)$', strng)
    
    if match:
        # Extract the trailing number part
        number_str = match.group(0)
        
        if number_str:
            # Find the leading zeros count
            leading_zeros = len(number_str) - len(number_str.lstrip('0'))
            # Convert the number to an integer and increment
            number = int(number_str)
            incremented_number = number + 1
            
            # Format the incremented number with the same number of leading zeros
            new_number_str = f'{incremented_number:0{len(number_str)}}'
            return strng[:match.start()] + new_number_str
        else:
            # If no trailing number, append '1'
            return strng + '1'
    else:
        # If no match (shouldn't occur due to the regex), just append '1'
        return strng + '1'







"""task2) Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.
Examples
[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2
"""

def solution(array_a, array_b):
    # Check if the arrays are of equal length
    if len(array_a) != len(array_b):
        raise ValueError("Both arrays must have the same length")
    
    # Compute the squared differences
    squared_diffs = [(a - b) ** 2 for a, b in zip(array_a, array_b)]
    
    # Calculate the average of squared differences
    average_squared_diff = sum(squared_diffs) / len(array_a)
    
    return average_squared_diff
