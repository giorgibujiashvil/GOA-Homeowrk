#task 1
money = int(input("enetr your Amount of money:"))

if money > 100:
    print("you have enough money to buy cloth:")
else:
    print("you dont have enought money:")

#task 2
age = int(input("enter your age:"))

if age > 20:
    print("adult")
else:
    print("kid")

#taks 3 

i = 0

while i <= 20:
    print(i)
    i = i + 2

#task 4

i = 100

while i >= 0:
    print(i)
    i = i - 1

#task 5
i = 1
sum = 0 

while i <= 100:
    sum = sum + 1
    i = i + 1

print(sum)

#task 6
i = 50 
sum = 0

while i <= 100:
    sum = sum +1
    i = i + 5

print(sum)

#task 7

num = int(input("enter your number:"))

while num % 2 == 0:
    num = num / 2 
    print(num)
    
