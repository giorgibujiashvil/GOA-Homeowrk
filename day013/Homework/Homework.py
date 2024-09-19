"""დაწერეთ პროგრამა, რომელიც ეკითხება მომხმარებლის ასაკს და შემდეგ დაბეჭდავს შეტყობინებას ასაკის მიხედვით: using(if-elif-else)"""
#მაგალითი1
#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
age = int(input("please enetr your age: "))

if age < 18:
    print("you are minor: ")
elif age >= 18 and age <65:
    print("you are an adult: ")
else:
    print("You are old: ")

#მაგალითი2
"""შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ დაბეჭდოს რიცხვი ლუწია თუ კენტი. გამოიყენეთ ფორ ციკლი, რომ სთხოვოთ მომხმარებელს 5 რიცხვი და შეამოწმეთ ხუთივე რიცხვი."""

for i in range(5):
    #შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
    number = int(input("please enter number: "))
    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number, "is odd: ")


#მაგალითი3
"""დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს ქულები ასოებით (A, B, C, D ან F) და შემდეგ დაბეჭდოს შეტყობინება ასოების მიხედვით: using(if-elif-else)
If the grade is A, print "Excellent!"
If the grade is B, print "Good job!"
If the grade is C, print "You passed."
If the grade is D, print "You can do better."
If the grade is F, print "You failed."""

#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
grade = input("please enter your grade: ")

if grade == "A":
    print("Excellent: ")
elif grade == "B":
    print("Good job: ")
elif grade == "C":
    print("you passed: ")
elif grade == "D":
    print("you can do better: ")
elif grade == "F":
    print("you failed: ")
else:
    print("Invalid grade entered: ")


#დავალება4 
"""დაწერეთ პროგრამა, რომელიც ბეჭდავს რიცხვებს 1-დან 10-მდე while ციკლის გამოყენებით"""

num = 1

while num < 10:
    print(num)
    num = num + 1    

#დავალება5
"""შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი 1-დან 10-მდე. გამოიყენეთ while loop, რათა გააგრძელოთ კითხვა, სანამ მომხმარებელი სწორად არ გამოიცნობს"""

num = 5
count = 0
number = 0

while number != num:
    #შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
    number = int(input("Please enter a number between 1 and 10 : "))
    count = count + 1
    if number == num:
        print("you guessed number in" ,count,"try")


#დავალება6
""" დაწერეთ პროგრამა, რომელიც დაბეჭდავს მოცემული რიცხვის (მაგ 5) პირველ 10 ჯერადს for loop-ის გამოყენებით."""

for i in range(5,50 + 1,5):
    print(i)
   

#მაგალითი7
"""შექმენით პროგრამა, რომელიც ბეჭდავს უკუთვლას 10-დან 1-მდე for loop-ის გამოყენებით."""

for i in range(10, 1, -1 ):
    print(i)


