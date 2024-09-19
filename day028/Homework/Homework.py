"""სახლში შესასრულებლად : codewars"""

"""task 1:
It's the academic year's end, fateful moment of your school report. The averages must be calculated. All the students come to you and entreat you to calculate their average for them. Easy ! You just need to write a script.

Return the average of the given array rounded down to its nearest integer.

The array will never be empty."""

def get_average(marks):
    total = sum(marks)
    return total // len(marks)

marks1 = [85, 90, 92, 88, 95]
print(get_average(marks1))

marks2 = [75, 80, 85, 90, 95]
print(get_average(marks2))




"""task 2:
In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?

Examples
make_negative(1);  # return -1
make_negative(-5); # return -5
make_negative(0);  # return 0:"""

def make_negative( number ):
    if number >= 0:
        return -number
    else:
        return number
    



"""task 3:
Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.

("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0"""


def str_count(strng, letter):
    return strng.count(letter)

# Test cases
print(str_count("Hello", 'o'))  
print(str_count("Hello", 'l'))  
print(str_count("", 'z'))



"""task 4:
In this kata you should simply determine, whether a given year is a leap year or not. In case you don't know the rules, here they are:

Years divisible by 4 are leap years,
but years divisible by 100 are not leap years,
but years divisible by 400 are leap years.
Tested years are in range 1600 ≤ year ≤ 4000."""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False










"""task 5:
Task
Given a string, return if all occurrences of a given letter are always immediately followed by the other given letter.

Worked Example
("he headed to the store", "h", "e") ➞ True

# All occurences of "h": ["he", "headed", "the"]
# All occurences of "h" have an "e" after it.
# Return True

('abcdee', 'e', 'e') ➞ False

# For first "e" we can get "ee"
# For second "e" we cannot have "ee"
# Return False"""
def check_following_letters(s, first_letter, second_letter):
    # Initialize a flag to track if we've seen the first letter
    seen_first_letter = False
    
    # Iterate through the string
    for char in s:
        if char == first_letter:
            # If we've already seen the first letter, check if the next character is the second letter
            if seen_first_letter:
                if s[s.index(char) + 1] != second_letter:
                    return False
            else:
                seen_first_letter = True
        elif char == second_letter:
            # If we encounter the second letter before the first, return False
            if not seen_first_letter:
                return False
    
    # If we reach this point, all occurrences of the first letter are followed by the second letter
    return True

# Test examples
print(check_following_letters("he headed to the store", "h", "e"))  # True
print(check_following_letters("abcdee", "e", "e"))





