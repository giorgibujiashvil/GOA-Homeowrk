#დათა თეზელაშვილი მიერ მოცემული დავალაბები

#while ციკლის დავალებები:

#მაგალითი1 Timer: დაწერეთ პროგრამა, რომელიც ითვლის 10-დან 1-მდე, დაბეჭდავს თითოეულ რიცხვს და შემდეგ დაბეჭდავს "დრო ამოიწურა". 
i = 10

while i >= 1:
    print(i)
    i = i - 1
print("time is up")

#მაგალითი2 რიცხვების ჯამი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვებს განუწყვეტლივ, სანამ ისინი არ შეიყვანენ 0-ს. შემდეგ დაბეჭდეთ ყველა შეყვანილი რიცხვის ჯამი.



#მაგალითი3 პაროლის შემოწმება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას. განაგრძეთ კითხვა, სანამ სწორი პაროლი არ იქნება შეყვანილი. დავუშვათ, რომ სწორი პაროლი არის "12345678".

password = int(input("enter your password:"))

while password != 12345678:
    #როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
    password = int(input("enter your password:"))

#მაგალითი4 ლუწი რიცხვები: დაწერეთ პროგრამა, რომელიც ბეჭდავს ყველა ლუწ რიცხვს 0-დან 20-მდე while ციკლის გამოყენებით.
i = 0

while i <= 20:
    print(i)
    i = i + 2


#მაგალითი5 დადებითი რიცხვები: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს უწყვეტად შეიყვანოს დადებითი რიცხვები, სანამ ისინი უარყოფით რიცხვს არ შეიყვანენ. შემდეგ დაბეჭდეთ ყველა შეყვანილი დადებითი რიცხვის ჯამი. 


sum_of_positive_numbers = 0

while True:
    number = float(input("Enter positive number (or  negative number to stop): "))
    
    if number < 0:
        break
    else:
        sum_of_positive_numbers += number

print("Sum of all positive numbers entered:", sum_of_positive_numbers)







#If statement დავალებები:
#მაგალითი6  შეამოწმეთ ლუწია თუ კენტი: დაწერეთ პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს და ბეჭდავს ლუწია თუ კენტი.

#როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
number = int(input("enter your number:"))

if number % 2 == 0:
    print("even")
else:
    print("odd")


#მაალითი7 ტემპერატურის კლასიფიკაცია: შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს ტემპერატურას ცელსიუსში. შემდეგ დაბეჭდეთ ცხელი (> 30°C), თბილი (20-30°C) ან ცივი (<20°C).

#როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
temperature = int(input("type your temperature in celsius:")) 

if temperature > 30:
    print("hot")
else:
    print("cold")


#მაგალითი8  ასოების შეფასება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოცდის ქულას. შემდეგ დაბეჭდეთ მათი ასოების შეფასება შემდეგი სკალის მიხედვით: A (90-100), B (80-89), C (70-79), D (60-69), F (< 60).

result = int(input("How many points did you get?:1"))

for a in range(90,100 + 1):
    if result == a:
        print("you got the highest point")
       

for b in range(80, 90):
    if result == b:
        print("you got a high point")
 

for c in range(70, 80):
    if result == c:
        print("you got an average point")

for d in range(60, 70):
    if result == d:
        print("you got a low point")

for c in range(0, 60):
    if result == c:
        print("you did not pass the point limit")







#მაგალითი9 შეამოწმეთ გაყოფა: შექმენით პროგრამა, რომელიც მომხმარებელს სთხოვს რიცხვს. შემდეგ დაბეჭდეთ, იყოფა თუ არა 2-ზე, 3-ზე ან ორივეზე.

#როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
number = int(input("enetr your number:"))

if number % 2 == 0 :
    print("gets divided")
else:
    print("not divided")

if number % 3 == 0:
    print("gets divided")
else:
    print("not diveded")


#მაგალითი10  რიცხვების შედარება: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ორ რიცხვს და შეადარებს მათ.

#როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number:"))

if num1 > num2:
    print("there is more:")
else:
    print("is less:")

if num1 < num2:
    print("there is more:")
else:
    print("is less:")


if num2 < num1:
    print("there is more:")
else:
    print("is less")


if num2 > num1:
    print("there is more:")
else:
    print("is less:")



#Combined (გამოიყენეთ while loop და if statement):
#მაგალითი11  რიცხვის გამოცნობა: დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს გამოიცნოს რიცხვი (მაგ., 5, ეს რიცხვი თქვენ აირჩიეთ). განაგრძეთ კითხვა, სანამ არ გამოიცნობენ სწორად.

number = int(input("enter your number:"))

while number != 5:
    #როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
    number = int(input("enter your number:"))





#მაგალით12  რიცხვების შემოწმება: შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს რიცხვს. სანამ ეს რიცხვი არ იქნება ლუწი, შეეკითხეთ მომხმარებელს თავიდან

#როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
number = int(input("enter your num:"))

while number % 2 != 0:
    number = int(input("enter your num:"))



#მაგალით13 რიცხვების კლასიფიკაცია: შექმენით პროგრამა, სადაც 50-იდან 100-ის ჩათვლით გამოიტანთ კენტ რიცხვებს. ციკლის გარეთ შექმენით ჯამის ცვლადი, სადაც დაემატება ციკლის ის რიცხვები, რომლებიც მეტია 75-ზე. ბოლოს დაპრინტეთ ამ ცვლადის მნიშვნელობა


sum = 0

for i in range(50, 100 + 1):
    if i % 2 != 0:
        print(i)
    if i > 75:
        sum = sum + i

print(sum)



#მაგალითი14 რიცხვების შედარება: მომხმარებელს შეეკითხეთ რიცხვი. სანამ ის ნაკლები იქნება მასზე 20-ით დიდ რიცხვზე, დაპრინტეთ ის.

#როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
number = int(input("Please enter a number: "))

while number <= 20:
    #როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
    number = int(input("Please enter a number greater than 20: "))

print(number)





#მაგალითი15 სახელის გამოცნობა. შექმენით ცვლადი სადაც იქნება შენახული თქვენი სახელი. მომხმარებელს შეეკითხეთ სახელი და სანამ თქვენსას არ შემოიტანს თავიდან შეეკითხეთ.

name = str(input("enter your name:"))

my_name = str("giorgi")

while my_name != name:
    name = str(input("enter your name:"))



#ბატონი ლუკა ცხვარაძის მიერ მოცემული დავალება:while ციკლში 5-5 მაგალითი

#მაგალითი1 

i = 0

while i <= 20:
    print(i)
    i = i + 2

#მაგალითი2
    
i = 100

while i >= 0:
    print(i)
    i = i - 1



#მაგალითი3
    
i = 1
sum = 0 

while i <= 100:
    sum = sum + 1
    i = i + 1

print(sum)



#მაგალითი4
    
i = 50 
sum = 0

while i <= 100:
    sum = sum +1
    i = i + 5

print(sum)



#მაგალითი5

#როგორ შემოვატანინოთ მომხმარებალს მნიშვნელობა
num = int(input("enter your number:"))

while num % 2 == 0:
    num = num / 2 
    print(num)






