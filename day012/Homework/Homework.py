#დათა თეზელშვილის მიერ მოცემული დავალებები

#მაგალითი1:დაწერეთ ალგორითმი რომელიც დაბეჭდავს დადებითია, უარყოფითი თუ ნულის ტოლი მომხმარებლის მიერ შემოტანილი რიცხვი.

#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
number = int(input("enetr your number:"))


    
if number > 0:
    print("the number is positive:")
elif  number < 0:
     print("the number is negative: ")  
else:
     print("number is zero:")

print("the text entered is not a matching number:")

#მაგალითი2:დაწერეთ ალგორითმი რომელიც მომხმარებელს შეთავაზებს ორ ოპერაციას: კილომეტრი - მილი, მილი - კილომეტრი. მომხმარებელმა უნდა აირჩიოს ერთ-ერთი მათგანი, ხოლო შემდეგ შეეკითხეთ რიცხვითი მნიშვნელობა, რომელზეც მოახდენთ მუშაობას და საბოლოოდ დაუბეჭდეთ უკვე გადაყვანილი მნიშვნელობა. თუ მომხმარებელი სწორად არ აირჩევს ოპერაციას, დაბეჭდეთ "Wrong decision".

print("1. km - miles")
print("2. miles - km")


#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
choice = int(input("please enter operetion number (1 or 2):"))
numebr = float(input("please enter number to convert it:"))

if choice == 1:
    print(numebr / 1.6)
elif choice == 2:
    print(number * 1.6)
else:
    print("wrong choice:")



#მაგალითი3:შექმენით რეგისტრაციის ალგორითმი. მომხმარებელს შეეკითხეთ სახელი, გვარი, ასაკი და მეილი, საბოლოოდ კი ერთ წინადადებაში გამოიტანეთ მიღებული ინფორმაცია

#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
name = str(input("enter your name:"))
surname = str(input("enter your surname:"))
age =str(input("enter your age:"))
gmail = str(input("enter your gmail:"))

print(name,surname,age,gmail)


#მაგალითი4:მომხმარებელს სამჯერ შეეკითხეთ რიცხვითი მნიშვნელობა და დაბეჭდეთ მათი საშუალო არითმეტიკული.

#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
num1 = int(input("please enter first numebr:"))
num2 = int(input("please enter second:"))
num3 = int(input("please enter third number:"))

result = (num1 + num2 + num3) / 3

print(result)



#მაგალითი5:მომხმარებელს შეეკითხეთ 1-იდან 9-ის ჩათვლით რომელიმე რიცხვი. შემდეგ გამოიყენეთ for ციკლი და გამოიტანეთ ამ რიცხვის ჯერადები 1-იდან 50-მდე დიაპაზონში.

#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
number = int(input("write any number from 1 to 9 inclusive:"))

for i in range(1, 50, + 1):
    if i % number == 0:
        print(i)



#მაგალითი6:მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის, ხოლო უდიდესი საბოლოო მნიშვნელობად გამოიყენეთ. ციკლში იტერაცია მოახდინეთ ერთით და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი).

#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
num1 = int(input("enter your first number:"))
num2 = int(input("enter your second number:"))

smallest = min(num1,num2)
largest = max(num1,num2)

for i in range(smallest,largest + 1):
    print(f"the cube of {i} is {i**3}:")


#მაგალითი7:მომხმარებელს შემოატანინეთ რიცხვი და დაბეჭდეთ მისი ციფრთა ჯამი.
    
# შემოვიტანოთ რიცხვი
number = input("შეიყვანეთ რიცხვი: ")

# გამოვთვალოთ ციფრთა ჯამი
total = sum(int(digit) for digit in number if digit.isdigit())

# დავბეჭდოთ შედეგი
print("sum_of_number:", total)



#მაგალითი8:დაწერეთ პროგრამა, რომელიც იღებს მომხმარებლისგან მთელ რიცხვს და დაბეჭდავს მის გამრავლების ცხრილს 10-ის ჩათვლით. მაგ: x, x2, x3 ... x*10.

#შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
number = int(input("enter an integer:"))

for i in range(1,10, + 1):
    print(f"{number} * {i} = {number * i}")


#მაგალითი9:შექმენით კალკულატორი, სადაც გექნებათ ოთხი ოპერაცია: + - / და გამრავლება (ფიფქი არ იწერება). მომხმარებელს შეეკითხებით ორ რიცხვს, შემდეგ სასურველ ოპერაციას და დაუბეჭდავთ გამოთვლილ მნიშვნელობას.
print ("Please select the operation")    
print ("1 - Add")    
print ("2 - Subtract")
print ("3 - Divide")     
print ("4 - Multiply")    
operacion = input("please enter choice: ")


num1 = int(input("enter first number for calculator: "))
num2 = int(input("enter second number for calculator: "))


if operacion == "1" :
    print(num1,"+", num2, "=", num1 + num2)

if operacion == "2" :
    print(num1,"-",num2,"=",num1 - num2)

if operacion == "3" :
    print(num1,"/",num2,"=",num1 / num2)

if operacion == "4": 
    print(num1,"x",num2,"=",num1 * num2)



#მაგალითი10:დაწერეთ პროგრამა, რომელიც იღებს სთრინგს, შემდეგ მომხმარებელს ეკითხება თუ რამდენჯერ განმეორდეს და for ციკლის გამოყენებით დაბეჭდეთ ის.

num = input("please enter number: ")
interacion = int(input("how mant times you want interacion:"))
for i in range(interacion):
    print(num)



#მაგალითი11:დაწერეთ პროგრამა, რომელიც გამოთვლის სხეულის მასის ინდექსს (BMI), მომხმარებლისგან მიღებული წონის (კილოგრამებში) და სიმაღლის (მეტრებში) გათვალისწინებით.მომხმარებელს შემოატანინეთ წელი და შეამოწმეთ ის ნაკიანი არის თუ არა.
    
height = int(input("please enter your height in meters:"))
weight = int(input("please enter your weight in kg:"))
bmi = weight / height

print("youre bmi =",bmi)



#მაგალითი12:მომხმარებელს შეეკითხეთ სამი რიცხვი და შეამოწმეთ არიან თუ არა პითაგორას რიცხვები
    
is_pythagorean_triplet = ("a,b,c")

 #შემოვატანინოთ მომხმარებელს რაიმე მნიშვნელობა
a = float(input("შეიყვანეთ პირველი გვერდი: "))
b = float(input("შეიყვანეთ მეორე გვერდი: "))
c = float(input("შეიყვანეთ მესამე გვერდი: "))

if is_pythagorean_triplet(a, b, c):
    print("შედეგი: ეს არის პითაგორის სამკუთხედი.")
else:
    print("შედეგი: ეს არ არის პითაგორის სამკუთხედი.")
    
    print("შეცდომა: გთხოვთ, შეიყვანოთ მხარეთა რიცხვები.")




#მაგალითი13:დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი 1-დან 5-ის ჩათვლით. თუ რიცხვი არის 1-ზე ნაკლები ან 5-ზე მეტი, დაბეჭდეთ "Invalid input". თუ რიცხვი 1-დან 5-ის ჩათვლითაა, დაბეჭდეთ "Valid input". 

number = int(input("enter number between 1-5: "))

if number < 1 or number > 5:
    print("Invalid input")
else:
    print("Valid input")






