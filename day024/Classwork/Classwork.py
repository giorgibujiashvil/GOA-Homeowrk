"""დავალებები vodewar-ში"""


"""8kyu"""

"""დავალება1:
Nathan loves cycling.

Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.

You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.

For example:

time = 3 ----> litres = 1

time = 6.7---> litres = 3

time = 11.8--> litres = 5"""
def litres(time):
    return int(time * 0.5)




"""დავალება2:
Your classmates asked you to copy some paperwork for them. You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

Example:
n= 5, m=5: 25
n=-5, m=5:  0"""
def paperwork(n, m):
    pass 

def paperwork(n, m):
    return n * m if n > 0 and m > 0 else 0



"""დავალება3:
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24"""
def grow(arr):
    pass

def grow(arr):
    m = 1
    for n in arr:
        m *= n
    return m



"""დავალება4:
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string"""
def fake_bin(x):
    result = ""
    
    for char in x:
        if int(char) < 5:
            result = result + "0"
        else:
            result = result + "1"
    
    return result







"""დავალება5:
Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language )."""
def count_by(x, n):
    multiples_x = []
    
    for i in range(x, x * n + 1):
        if i % x == 0:
            multiples_x.append(i)
    
    return multiples_x





"""7kyu"""

"""დავალება6:
Jaden Smith, the son of Will Smith, is the star of films such as The Karate Kid (2010) and After Earth (2013). Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word, check out how contractions are expected to be in the example below.

Your task is to convert strings to how they would be written by Jaden Smith. The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them."""

def to_jaden_case(string):
    return ' '.join(word.capitalize() for word in string.split())





"""დავალება7:
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z."""
def accum(st):
    result = ""
    for i, char in enumerate(st):
        result += char.upper() + char.lower() * i
        if i != len(st) - 1:
            result += "-"
    return result








"""დავალება8:
The museum of incredibly dull things
The museum of incredibly dull things wants to get rid of some exhibits. Miriam, the interior architect, comes up with a plan to remove the most boring exhibits. She gives them a rating, and then removes the one with the lowest rating.

However, just as she finished rating all exhibits, she's off to an important fair, so she asks you to write a program that tells her the ratings of the exhibits after removing the lowest one. Fair enough.

Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with the lowest index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]
LISTSARRAYSFUNDAMENTALS"""
def remove_smallest(numbers):
    if not numbers:
        return []
    
    min_index = numbers.index(min(numbers))
    return numbers[:min_index] + numbers[min_index+1:]






"""დავალება10:
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"""
def likes(names):
    count = len(names)
    if count == 0:
        return "no one likes this"
    elif count == 1:
        return f"{names[0]} likes this"
    elif count == 2:
        return f"{names[0]} and {names[1]} like this"
    elif count == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"
    else:
        return f"{names[0]}, {names[1]} and {count - 2} others like this"

















































"""6kyu"""


"""დავალება9:
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Additionally, if the number is negative, return 0.

Note: If the number is a multiple of both 3 and 5, only count it once."""
def solution(number):
    if number <= 0:
        return 0
    
    sum_multiples = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    
    return sum_multiples








"""დავალება7:
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""

