"""8kyu"""

"""დავალება1:
Your function takes two arguments:

current father's age (years)
current age of his son (years)
Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future."""


def twice_as_old(dad_years_old, son_years_old):
    age_difference = dad_years_old - 2 * son_years_old
    return abs(age_difference)


print(twice_as_old(36, 7))  
print(twice_as_old(55, 30))  
print(twice_as_old(42, 21))  
print(twice_as_old(22, 1))



"""დავალება2:
Create a function that takes 2 integers in form of a string as an input, and outputs the sum (also as a string):

Example: (Input1, Input2 -->Output)

"4",  "5" --> "9"
"34", "5" --> "39"
"", "" --> "0"
"2", "" --> "2"
"-5", "3" --> "-2"
Notes:

If either input is an empty string, consider it as zero.

Inputs and the expected output will never exceed the signed 32-bit integer limit (2^31 - 1"""
def sum_str(a, b):
    a = int(a) if a else 0
    b = int(b) if b else 0
    
    result = a + b
    
    
    return str(result)

# Test cases
print(sum_str("4", "5"))  
print(sum_str("34", "5")) 
print(sum_str("", ""))     
print(sum_str("2", ""))  
print(sum_str("-5", "3"))





"""დავალება3:
Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]"""
def reverse_seq(n):
    return list(range(n, 0, -1))


print(reverse_seq(5))




"""დავალება4:
Write a function that removes the spaces from the string, then return the resultant string.

Examples:

Input -> Output
"8 j 8   mBliB8g  imjB8B8  jl  B" -> "8j8mBliB8gimjB8B8jlB"
"8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"
"8aaaaa dddd r     " -> "8aaaaaddddr"""
def no_space(x):
    return x.replace(" ", "")




"""დავალება5:
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F"""
def abbrev_name(name):
    first_name, last_name = name.split()
    
    abbreviated = f"{first_name[0].upper()}.{last_name[0].upper()}"
    
    return abbreviated


print(abbrev_name("Sam Harris"))       
print(abbrev_name("patrick feeney"))



"""7kyu"""

"""დავალება6:
Your task is to write function factorial."""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5)) 


"""დავალება7:
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust)."""
def divisors(integer):
    divisors_list = []
    for i in range(2, integer):
        if integer % i == 0:
            divisors_list.append(i)
    if len(divisors_list) == 0:
        return "{} is prime".format(integer)
    else:
        return divisors_list


print(divisors(12))
print(divisors(13))
print(divisors(25))




"""დავალება8:
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.

Examples (input --> output)
4 --> 3 // we have 3 divisors - 1, 2 and 4
5 --> 2 // we have 2 divisors - 1 and 5
12 --> 6 // we have 6 divisors - 1, 2, 3, 4, 6 and 12
30 --> 8 // we have 8 divisors - 1, 2, 3, 5, 6, 10, 15 and 30
Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to see which numbers are counted in each case."""

import math

def divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2  
    return count


print(divisors(4))  
print(divisors(5))  
print(divisors(12)) 
print(divisors(30)) 









"""დავალება9:
Instructions
Write a function that takes a single non-empty string of only lowercase and uppercase ascii letters (word) as its argument, and returns an ordered list containing the indices of all capital (uppercase) letters in the string.

Example (Input --> Output)
"CodEWaRs" --> [0,3,4,6]"""
def capitals(word):
    indices = []
    for index, char in enumerate(word):
        if char.isupper():
            indices.append(index)
    return indices


print(capitals("CodEWaRs"))



"""დავალება10:
In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:

make as few changes as possible.
if the string contains equal number of uppercase and lowercase letters, convert the string to lowercase.
For example:"""
def solve(s):
    uppercase_count = sum(1 for char in s if char.isupper())
    lowercase_count = sum(1 for char in s if char.islower())
    
    if uppercase_count == lowercase_count or lowercase_count > uppercase_count:
        return s.lower()
    else:
        return s.upper()


print(solve("CodEWaRs"))


