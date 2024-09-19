"""task 1: Write a small function that returns the values of an array that are not odd.

All values in the array will be integers. Return the good values in the order they are given.
"""

def no_odds(values):
    return [value for value in values if value % 2 == 0]


values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = no_odds(values)
print(result)  
    

"""task 2: Write a function that takes a positive integer n, sums all the cubed values from 1 to n (inclusive), and returns that sum.

Assume that the input n will always be a positive integer.

Examples: (Input --> output)

2 --> 9 (sum of the cubes of 1 and 2 is 1 + 8)
3 --> 36 (sum of the cubes of 1, 2, and 3 is 1 + 8 + 27)"""

def sum_cubes(n):
    return sum(i**3 for i in range(1, n + 1))


print(sum_cubes(2))  
print(sum_cubes(3))


"""task 3: Write a function that returns the number of occurrences of an element in an array.

Examples
sample = [0, 1, 2, 2, 3]
number_of_occurrences(0, sample) == 1
number_of_occurrences(4, sample) == 0
number_of_occurrences(2, sample) == 2
number_of_occurrences(3, sample) == 1"""

def number_of_occurrences(element, sample):
    return sample.count(element)

sample = [0, 1, 2, 2, 3]
print(number_of_occurrences(0, sample))  
print(number_of_occurrences(4, sample))  
print(number_of_occurrences(2, sample))  
print(number_of_occurrences(3, sample))