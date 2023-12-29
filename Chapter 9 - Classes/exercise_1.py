from exercise_0 import *

restaurant_1 = Restaurant('Chez Panisse', 'California farm-to-table')
print(f'Name: {restaurant_1.restaurant_name}.\n')
print(f'Cuisine type: {restaurant_1.cuisine_type}.\n')
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

restaurant_2 = Restaurant('McDonald\'s', 'Fast Food')
restaurant_3 = Restaurant('The French Laundry', 'Fine dining')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

user_1 = User('Istrate', 'Mihai Septimius', 'i.mihai9960@gmail.com', 27)
user_2 = User('Popescu', 'Ion', 'p.ion9940@gmail.com', 29)

user_1.greet_user()
user_1.describe_user()

print('------------------------------------')

user_2.greet_user()
user_2.describe_user()
