from exercise_0 import *

restaurant = Restaurant('Chez Panisse', 'California farm-to-table')
print(f'Number of served customers: {restaurant.number_served}.')
restaurant.number_served = 10
print(f'Number of served customers: {restaurant.number_served}.')
restaurant.set_number_served(20)
print(f'Number of served customers: {restaurant.number_served}.')
restaurant.increment_number_served(-20)
restaurant.increment_number_served(20)
print(f'Number of served customers: {restaurant.number_served}.')

user_1 = User('Istrate', 'Mihai Septimius', 'i.mihai9960@gmail.com', 27)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f'Users\'s {user_1.last_name} {user_1.first_name} login atetempts are: {user_1.login_attempts}.')
user_1.reset_login_attempts()
print(f'Users\'s {user_1.last_name} {user_1.first_name} login atetempts are: {user_1.login_attempts}.')
