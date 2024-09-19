"""ყველამ შეასრულეთ classwork-ის ამოცანები:

8 kyu:"""


"""task 1:You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow.

"""
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "Invalid input"  

current_state = "green"
next_state = update_light(current_state)
print("Next state:", next_state)





"""task 2: In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code."""

def find_difference(a, b):
    return abs((a[0] * a[1] * a[2]) - (b[0] * b[1] * b[2]))




"""task 3: Triple Trouble
Create a function that will return a string that combines all of the letters of the three inputed strings in groups. Taking the first letter of all of the inputs and grouping them next to each other. Do this for every letter, see example below!

E.g. Input: "aa", "bb" , "cc" => Output: "abcabc"

Note: You can expect all of the inputs to be the same length."""


def triple_trouble(one, two, three):
    combined = ""
    for i in range(len(one)):
        combined += one[i] + two[i] + three[i]
    return combined

input_one = "aa"
input_two = "bb"
input_three = "cc"
output = triple_trouble(input_one, input_two, input_three)
print("Output:", output)



"""7kyu:"""

"""task 4: Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:(Input1, Input2, Input3 --> Output)

5, 2, "add"      --> 7
5, 2, "subtract" --> 3
5, 2, "multiply" --> 10
5, 2, "divide"   --> 2.5"""

def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
    else:
        return "Invalid operator"

result = arithmetic(5, 2, "add")
print("Result:", result)










"""task 5: Are the numbers in order?
In this Kata, your function receives an array of integers as input. Your task is to determine whether the numbers are in ascending order. An array is said to be in ascending order if there are no two adjacent integers where the left integer exceeds the right integer in value.

For the purposes of this Kata, you may assume that all inputs are valid, i.e. arrays containing only integers.

Note that an array of 0 or 1 integer(s) is automatically considered to be sorted in ascending order since all (zero) adjacent pairs of integers satisfy the condition that the left integer does not exceed the right integer in value.

For example:

in_asc_order([1,2,4,7,19]) # returns True
in_asc_order([1,2,3,4,5]) # returns True
in_asc_order([1,6,10,18,2,4,20]) # returns False
in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order
"""

def in_asc_order(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

input_array = [1, 2, 3, 4, 5]
print(in_asc_order(input_array))




"""task 6: We want to generate a function that computes the series starting from 0 and ending until the given number.

Example:
Input:

> 6
Output:

0+1+2+3+4+5+6 = 21

Input:

> -15
Output:

-15<0

Input:

> 0
Output:

0=0"""

def show_sequence(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return f"{n}<0"
    else:
        sequence = "+".join(str(i) for i in range(n + 1))
        total = sum(range(n + 1))
        return f"{sequence} = {total}"


print(show_sequence(6))




"""6kyu"""



"""task 7: Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"""


def to_weird_case(words):
    word_list = words.split()

    for i in range(len(word_list)):
        word = word_list[i]
        new_word = ''.join(c.upper() if idx % 2 == 0 else c.lower() for idx, c in enumerate(word))
        word_list[i] = new_word

    return ' '.join(word_list)

print(to_weird_case("String")) 
print(to_weird_case("Weird string case"))





"""task 8:
Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
Note: In the C and NASM languages you are given the third parameter which is the number of segment blocks."""
def data_reverse(data):
    segments = [data[i:i+8] for i in range(0, len(data), 8)]
    reversed_segments = segments[::-1]
    return [bit for segment in reversed_segments for bit in segment]

input_data = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
output_data = data_reverse(input_data)
print(output_data)






