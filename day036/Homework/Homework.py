"""დავალება1"""    """codewars"""

"""პირობა  :  You're running an online business and a big part of your day is fulfilling orders. As your volume picks up that's been taking more of your time, and unfortunately lately you've been running into situations where you take an order but can't fulfill it.

You've decided to write a function fillable() that takes three arguments: a dictionary stock representing all the merchandise you have in stock, a string merch representing the thing your customer wants to buy, and an integer n representing the number of units of merch they would like to buy. Your function should return True if you have the merchandise in stock to complete the sale, otherwise it should return False.

Valid data will always be passed in and n will always be >= 1."""

def fillable(stock, merch, n):
    """
    Check if there's enough stock to fulfill the order.

    Args:
    - stock (dict): A dictionary representing the stock of merchandise, where keys are merchandise names and values are integers (quantity in stock).
    - merch (str): The name of the merchandise the customer wants to buy.
    - n (int): The number of units of merchandise the customer wants to buy.

    Returns:
    - bool: True if there's enough stock to fulfill the order, False otherwise.
    """
    if merch in stock and stock[merch] >= n:
        return True
    else:
        return False
    


"""დავალება2"""

"""პირობა  :  You're putting together contact information for all the users of your website to ship them a small gift. You queried your database and got back a list of users, where each user is another list with up to two items: a string representing the user's name and their shipping zip code. Example data might look like:

[["Grae Drake", 98110], ["Bethany Kok"], ["Alex Nussbacher", 94101], ["Darrell Silver", 11201]]
Notice that one of the users above has a name but doesn't have a zip code.

Write a function user_contacts() that takes a two-dimensional list like the one above and returns a dictionary with an item for each user where the key is the user's name and the value is the user's zip code. If your data doesn't include a zip code then the value should be None.

For example, using the input above, user_contacts() would return this dictionary:

{
    "Grae Drake": 98110,
    "Bethany Kok": None,
    "Alex Nussbacher": 94101,
    "Darrell Silver": 11201,    
}
You don't have to worry about leading zeros in zip codes"""

def user_contacts(data):
    """
    Converts a list of user data into a dictionary of user contacts.

    Args:
    - data (list of list): A two-dimensional list where each inner list contains either one or two items: 
                           [user's name, optional user's zip code].

    Returns:
    - dict: A dictionary where keys are user names and values are user zip codes (or None if zip code is not provided).
    """
    contacts = {}
    for item in data:
        if len(item) == 2:
            contacts[item[0]] = item[1]
        elif len(item) == 1:
            contacts[item[0]] = None
    return contacts



"""დავალება3"""

"""პირობა  : You probably know that the "mode" of a set of data is the data point that appears most frequently. Looking at the characters that make up the string "sarsaparilla" we can see that the letter "a" appears four times, more than any other letter, so the mode of "sarsaparilla" is "a".

But do you know what happens when two or more data points occur the most? For example, what is the mode of the letters in "tomato"? Both "t" and "o" seem to be tied for appearing most frequently.

Turns out that a set of data can, in fact, have multiple modes, so "tomato" has two modes: "t" and "o". It's important to note, though, that if all data appears the same number of times there is no mode. So "cat", "redder", and [1, 2, 3, 4, 5] do not have a mode.

Your job is to write a function modes() that will accept one argument data that is a sequence like a string or a list of numbers and return a sorted list containing the mode(s) of the input sequence. If data does not contain a mode you should return an empty list.

For example:

>>> modes("tomato")
["o", "t"]
>>> modes([1, 3, 3, 7])
[3]
>>> modes(["redder"])
[] """


def modes(data):
    """
    Finds the mode(s) of the input sequence (string or list).

    Args:
    - data (str or list): The input sequence for which modes need to be found.

    Returns:
    - list: A sorted list containing the mode(s) of the input sequence. If there are multiple modes, they are all included.
            If there are no modes (all elements have the same frequency), returns an empty list.
    """
    if isinstance(data, str):
        # If data is a string, convert it to a list of characters
        data = list(data)
    
    # Create a dictionary to count frequencies of each element
    frequency = {}
    for item in data:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    
    # Find the maximum frequency
    max_frequency = max(frequency.values())
    
    # Gather all elements that have the maximum frequency
    modes_list = [item for item, freq in frequency.items() if freq == max_frequency]
    
    # Sort the modes_list alphabetically (for strings) or numerically (for numbers)
    modes_list.sort()
    
    # Return the sorted list of modes, or an empty list if there are no modes
    if max_frequency > 1:
        return modes_list
    else:
        return []




"""დავალება4"""

"""პირობა  : შექმენით dictionary რმელსაც დაარქმევდთ student და გადასცემთ შესაბამის key და value """

def create_student_info(name, age, major):
    student = {
        "name": name,
        "age": age,
        "major": major
    }
    return student

student_info = create_student_info(22)

print(student_info)



"""დავალება5"""

"""პირობა  :  შექმენით ცვლადი რომელსაც დავარქმევთ result და for ციკლის გამოყენებით results დავუმატებთ student vales და დავპრინტავთ"""



results = []

for i in range(3):  
    name = input("სტუდენტის სახელი: ")
    age = int(input("ასაკი: "))
    major = input("სწორება: ")

    student_info = {
        "name": name,
        "age": age,
        "major": major
    }

    results.append(student_info)


print("სტუდენტების შედეგები:")
for student in results:
    print(f"სახელი: {student['name']}, ასაკი: {student['age']}, სწორება: {student['major']}")

