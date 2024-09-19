"""დავალება: შექმენით ორი სია, პირველში საყვარელი ადამიანების სახელები, ხოლო მეორეში ფავორიტი მანქანები ჩაწერეთ. ორივე სიაში 5 ელემენტი უნდა გქონდეთ. თავდაპირველად დაბეჭდეთ ორივე სია, შემდეგ გამოიყენეთ ინდექსები და დაბეჭდეთ კონკრეტული ელემენტები"""

favorite_people_name = [
    "girogi",
    "dato",
    "nika",
    "lado",
    "irakli",
]

favorite_cars_name = [
    "bmw",
    "mersedec",
    "audi",
    "lamborgini",
    "ferrari",
]

print("favorite_cars_name",favorite_cars_name)
print("favorite_people_name",favorite_people_name)

print(favorite_cars_name[3])
print(favorite_people_name[0])


"""დავალება: შექმენით ორი სთრინგი, პირველში შეინახეთ თქვენი სახელი, ხოლო მეორეში გვარი. საბოლოოდ გამოიტანეთ თქვენი ინიციალები - სახელის პირველი ასო + . + გვარის პირველი ასო"""

my_name = "giorgi"
my_surname = "bujiashvili"

print(my_name[0],".",my_surname[0])




"""დავალება:შექმენი სია, სადაც გექნება 1-იდან 10-ის ჩათვლით რიცხვები. შემდეგ ლუწ ინდექსებზე მყოფი ელემენტების ადგილას -1 დაწერე"""


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(len(numbers)):
    if i % 2 != 0:
        numbers[i] = -1

print(numbers)




"""დავალება: შექმენით ორი სია, უნდა გქონდეთ ორივე განსხვავებული ზომის. len ფუნქციის გამოყენებით გაიგეთ მათი სიგრძე"""

list1 = [5,7,2,4,6,1,8,10]
list2 = [3,4,5,6,7,1]

print(len(list1))
print(len(list2))

"""დავალება:len ფუნქციის გამოყენებით გამოიტანეთ თქვენი გვარის ბოლო ასო"""

surname = "bujiashvili"

print(surname[len(surname)-1][-1])

"""დავალება:გააერთიანეთ ერთ სია მეორე სიასთან"""

print(list1 + list2)