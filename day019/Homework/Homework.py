#დავალება1:
""" შექმენით ლისტი სადაც ჩამოწერილიქნება თამაშის სახელები და შემდგომ თამაშებს ვანაცვლებთ სოლოლერნით , w3 , codewars - ებით და ასეშემდეგ."""

game_list = [
    "DAYZ",
    "GTA 5",
    "CS GO 2",
]

game_lists1 = "sololearn" 
game_lists2 = "codewar"
game_lists3 = "w3"

all_game_lists = game_lists1,game_lists2,game_lists3

print(all_game_lists)


#დავალება2:
"""შექმენით 5 ინფუთი და ამ ინფუთებით შეადგინეთ სია, შემდეგ გამოიტანეთ ამ სიიდან ლუწი რიცხვები, ისე რომ ლოგიკამ ყველა შემთხვევაში იმუშაოს."""

input1 = 6
input2 = 13
input3 = 7
input4 = 25
input5 = 4

list = [input1,input2,input3,input4,input5]
even_num = [number for number in list if number % 2 == 0]

print(even_num)

