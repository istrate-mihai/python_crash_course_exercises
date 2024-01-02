from user import User

from admin import Admin

user_1 = User('Istrate', 'Mihai Septimius', 'i.mihai9960@gmail.com', 27)
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

print(f'Users\'s {user_1.last_name} {user_1.first_name} login atetempts are: {user_1.login_attempts}.')
user_1.reset_login_attempts()
print(f'Users\'s {user_1.last_name} {user_1.first_name} login atetempts are: {user_1.login_attempts}.')

user_2 = User('Popescu', 'Ion', 'p.ion9940@gmail.com', 29)

user_1.greet_user()
user_1.describe_user()

print('------------------------------------')

user_2.greet_user()
user_2.describe_user()

admin = Admin('Istrate', 'Mihai', 'i.mihai9960@gmail.com', 27, ['can add post', 'can delete post', 'can ban user'])
admin.privileges.show_privileges()
