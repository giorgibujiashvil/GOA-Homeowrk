#my numbers
weight = 50
height = 170

required_weight = int(input("enter your weight:"))
required_height = int(input("rnter your height:"))

#the number entered by the user
users_weight = 50
users_height = 170

#the number entered by the user is equal to my number
print(required_weight == users_weight)
print(height == required_height)


#and 
print(weight == required_weight and height == required_height)
print(weight <= required_weight and height <= required_height)
#or
print(weight >= required_weight or height >= required_height)
print(weight == required_weight or height == required_height)


pushups = 30
squats = 50

required_pushups = int(input("enter your pushups number:"))

requierd_squats = int(input("enter your squats number:"))

print(pushups == required_pushups and squats == requierd_squats)

incoming_pushab_number = 30
incoming_squats_number = 50

print(pushups == incoming_pushab_number)
print(squats == incoming_squats_number)