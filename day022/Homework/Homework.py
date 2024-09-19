"""დავალება1:
შექმენით ფუნქცია სახელად numbers_product. ფუნქციას გადაეცით სამი არგუმენტი - start, end, step. შემდეგ გამოიყენეთ while ციკლი (for ციკლი არ შეიძლება) და სიაში დაამატეთ რიცხვები - დაიწყეთ start-იდან, იტერაცია მოახდინეთ step-ით და ციკლი ამუშავეთ end-ამდე. განიხილეთ ეს სია და მოახდინეთ მასზე ფილტრაცია, კიდევ ახალ სიაში დაამატეთ მარტო 3-ის ჯერადი რიცხვები. საბოლოოდ დააბრუნეთ 3-ის ჯერადების სიის ყველა რიცხვის ნამრავლი - product."""
def numbers_product(start, end, step):
    numbers = []
    current_number = start
    
    while current_number <= end:
        numbers.append(current_number)
        current_number += step
    
    filtered_numbers = [num for num in numbers if num % 3 == 0]
    
    product = 1
    for num in filtered_numbers:
        product *= num
    
    return product

print(numbers_product(1, 10, 2))




"""დავალება2:
პირველ დავალებაში მიღებული შედეგი შეინახეთ ცვლადში. შემდეგ შექმენით ახალი ფუნქცია, სადაც ამ რიცხვზე მოახდენთ მათემატიკურ მოქმედებებს: +, -, *, /. აუცილებელია, რომ მომხმარებელს შემოატანინოთ მეორე რიცხვი და შემდეგ მოახდინოთ მათემატიკური მოქმედებები."""

num = 27

number = int(input("enetr randon number: "))

numebrs = num + number
numebrs = num - number
numbers = num * number
numebrs = num / number

print(numbers)





"""დავალება3:
შექმენით ფუნქცია სახელად hashtag generator. მომხმარებელს შეეკითხეთ წინადადება და ის გადაეცით არგუმენტად ფუნქციას. მუშაობის წესები: საბოლოო ვერსია იწყება #-თი, სიტყვები შეერთებულია, ყველა სიტყვა იწყება დიდი ასოთი. Test case:
"abc def ghi" -> "#AbcDefGhi"""
def hashtag_generator(phrase):
  
    words = phrase.split()  # სიტყვების გაყოფა
    capitalized_words = [word.capitalize() for word in words]  
    hashtag = '#' + ''.join(capitalized_words)  
    return hashtag

# ფუნქციის ტესტირება
test_phrase = "abc def ghi"
print(hashtag_generator(test_phrase)) 




""" დავალება4:
შექმენით ფუნქცია სახელად num_divisors. ამ სიას არგუმენტად გადაეცით მომხმარებლის მიერ შემოტანილი მთელი რიცხვი. თქვენი დავალებაა, რომ დააბრუნოთ სია, სადაც იქნება ამ რიცხვის ყველა გამყოფი. Test case: 20 -> [1, 2, 4, 5, 10, 20]"""
def num_divisors(number):
    divisors = []  
    
   
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)  
            
    return divisors


test_number = 20
print(num_divisors(test_number))




"""დავალება5:
შექმენით ფუნქცია manual_split. ამ ფუნქციაში უნდა შეიმუშავოთ split-ის მსგავსი ალგორითმი, მაგრამ არ გამოიყენოთ split. შესაბამისად ფუნქციას არგუმენტად გადაეცით მომხმარებლის შემოტანილი სიტყვა. ასევე მომხმარებელს შეეკითხეთ start, end, step  და ეს მონაცემები გამოიყენეთ სიტყვაზე სამუშაოდ."""
def manual_split(string, start=0, end=None, step=1):
    if end is None:
        end = len(string) 
        
    result = []  
    
    
    for i in range(start, end, step):
        result.append(string[i])  
        
    return ''.join(result)  

test_string = "abcdefg"
print(manual_split(test_string, 1, 5, 2))