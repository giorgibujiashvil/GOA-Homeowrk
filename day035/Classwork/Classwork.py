"""1) შექმენით სია და დაამატეთ თქვენი მეგობრების სახელები append ის გამოყენებით."""

names = ["nodo", "gio", "dato"]

names.append("nika")

print(names)


"""2)შექმენით სია და ყველა ელემენტი წაშალეთ (გაასუფთავეთ)"""

car_list = ["bmw", "honda", "audi"]

car_list.clear()

print(car_list)


"""3) შექმენით სია და დააკოპიერთ ეგ სია შემდეგ კი შეინახეთ მეორე ცვლადში"""

list = [1,2,3,4,5,6,7,8,9,10]

cop_list = list.copy()

print(cop_list)
print(list)


"""4) შექმენით სახელების სია და დათალეთ რამდენჯერ მეორდება თვქენი სასურველი სახელი სიაში"""

name = "nika gio lado sandro."

x = name.find("o")

print(x)



"""5) შექმენით სია და იპოვეთ კონკრეტული თქვენი სასურველი ელემენტის ინდექსი"""

list = [1,2,3,4,5]

index = list.index(5)

print(index)


"""6) შექმენით სია და ჩასვით 3 ინდექსზე ახალი მნიშვნელობა"""

list = [2,4,6,8,10]

list[3] = 5

print(list)



"""7) წაშალეთ სიის ბოლოში და სიის დასწყიშვი ელემენტები"""

list = [1,3,5,7,9]

list = list[1:5]

print(list)



"""8) წაშალეთ ელემენტი remove მეთოდის გამოყენებით"""

list = [1,2,4,6,7,8,9]

list.remove(7)

print(list)



"""9) შემოაბრუნეთ სია"""

list = ["lambo","ferrari","bently","rolls royce"]

list.reverse()

print(list)


"""10) დაალაგეთ რიცხვების სია ზრდადობით"""

num_list = [3,7,6,4,8,5]

num_list.sort()

print(num_list)


"""11) გააფართოვეთ პირველი სია მეორე სიით"""

list1 = [1,2,3,4,5]

list2 = [6,7,8,9,10]

list2 = list2.copy()

list1.sort()

print(list1)
print(list2)


