"""დავალება1: შექმენით range-ის კოპიო ფუნქცია - my_range. მას გადაეცემა start, end, step. ფუნქციაში შემდეგ შექმენით სია, სადაც გექნებათ start-სა და step-ს შორის არსებული რიცხვები, გაითვალისიწინეთ step. არ გამოიყენოთ range()"""

def my_sum(numbers):
    numbers = [1,2,3,4,5]

    sum = 0 

    for num in numbers:
        sum += num

        print(sum)

my_sum([1,2,3,4,5])

"""დავალება2: შექმენით ფუნქცია სახელად my_filter, რომელსაც გადაეცემა ერთი სია და სიმბოლო, რომელიც სიიდან ამოიშლება. საბოლოოდ დააბრუნეთ სია, სადაც არ იქნება არც ერთი ეს სიმბოლო"""
def my_filter(lst, symbol):
    
    filtered_list = [item for item in lst if item != symbol]
    return filtered_list


test_list = [1, 2, 3, 4, 5, 6]
symbol_to_remove = 3
print(my_filter(test_list, symbol_to_remove))


"""დავალება3: შექმენით ფუნქცია, რომელსაც გადაეცემა სია. თქვენი დავალებაა, რომ ამ სიის დადებითი რიცხვების ნამრავლი დააბრუნოთ"""
def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

test_list = [1, 2, 3, 4, 5]
print(multiply_list(test_list))


"""დავალება4: შექმენით ფუნქცია სახელად greet, რომელსაც გამოძახებისას გადასცემთ მომხმარებლის სახელს - დაბეჭდავს "Welcome მომხმარებლის სახელი აქ!". """

def welcome(name):
    print("welcome <3",name)

welcome("giorgi")



"""დავალება5: შექმენით ფუნქცია, რომელსაც გადაეცემა ერთ სია. ამ სიაში უნდა გაიგოთ კენტი რიცხვების ჯამი. საბოლოოდ კი მიღებული შედეგი გამოიყენეთ ფუნქციის გარეთ, მიუმატეთ 5 და დაბეჭდეთ"""

def odd_num(list):
    odd_sum = 0 
    for num in list:
        if num % 2 != 0:
            odd_sum += num 
    return odd_sum

my_list = [1,2,3,4,6,7,9,10,20]

odd_sum_result = odd_num(my_list)

final_result = odd_sum_result + 5

print(final_result)
print(odd_sum_result)