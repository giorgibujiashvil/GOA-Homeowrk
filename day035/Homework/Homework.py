"""შეეცადეთ რომ გააკეთოთ ამ მეთოდების კოპიუ ფუნქციები"""

"""1) list methods: append(),  clear(), copy(), count(), index(), insert(), pop(), remove(), reverse(), sort(),  len(), extend() """

"""task:1:append()"""

car_list = ["audi","bmw"]

car_list.append("civic")

print(car_list)


"""task:2:clear()"""

num_list = [1,2,3,4,5,6,7,8,9,10]

num_list.clear()

print(num_list)


"""task:3:copy()"""


list1 = [5,6,7,8,9,10]

list2 = [11,12,13,14,15]

list2 = list2.copy()

list1.sort()

print(list1)
print(list2)



"""task:4:count()"""

fruit = ["apple","banana","oringe" "apple"]

x = fruit.count("apple")

print(x)



"""task:5:index()"""

list = [1,2,3,4,5]

x = list.index(2)

print(x)



"""task:6:insert()"""

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits)


"""task:7:pop()"""

fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)


"""task:8:remove()"""

list = [2,4,6,8,]

list.remove(4)

print(list)


"""task:9:reverse()"""

num_list = [5,6,7,8,9,10]

num_list.reverse()

print(num_list)


"""task:10:sort()"""

car_list = ["bently","audi","bmw"]

car_list.sort()

print(car_list)

"""task:11:len()"""

fruit_list = ["apple", "orange", "cherry"]

x = len(fruit_list)

print(x)




"""task:12:extend() """

fruits = ['bluebery', 'banana', 'cherry']

cars = ['audi', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)



"""2) string methods:  capitalize(),     count(),      count(),     find(),   index(),    isalnum(),   isalpha(),  isdigit(),  islower(),  isupper(),  lower(),  replace(),   split(),  startswith(),  endswith() ,  swapcase(),  """

"""task:1:capitalize() """

name = "goa is best"

text = name.capitalize()

print (text)




"""task:2:count()"""

car = ["bmw","ford","volvo"]

x = fruit.count("volvo")

print(x)


"""task:3:find()"""

text = "goal oriented academy"

x = text.find("goal")

print(x)



"""task:4:index()"""

list = [1,2,3,4,5]

index = list.index(5)

print(index)


"""task:5:isalnum()"""

name = "girogi12"

x = name.isalnum()

print(x)


"""task:6:isalpha()"""

car = "mercedes_benz"

x = car.isalnum()

print(x)


"""task:7:isdigit()"""

num = "12,13,14,15,"

x = num.isdigit()

print(x)


"""task:8:islower()"""

text = "hello"

x = text.islower()

print(x)



"""task:9:isupper()"""

big_nums = "123"

x = big_nums.isupper()

print(x)



"""task:10:lower()"""

text = "HEllo"

x = text.lower()

print(x)



"""task:11:replace()"""

text = "I like bananas"

x = text.replace("bananas", "apples")

print(x)



"""task:12:split()"""

text = "welcome to the jungle"

x = text.split()

print(x)


"""task:13:startswith()"""

text = "hello world"

x = text.startswith("hello")

print(x)



"""task:14:endswith()"""

text = "Goa"

x = text.endswith("Goa")

print(x)


"""task:15:swapcase()"""
text = "Hello My Name Is PETER"

x = text.swapcase()

print(x)






