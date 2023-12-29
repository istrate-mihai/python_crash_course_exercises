user_list = ['user_1', 'user_2', 'user_3', 'user_4', 'admin']

for user in user_list:
    if user == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print('Hello ' + user + ', thank you for logging in again.')

user_list = []

if len(user_list) < 1:
    print('We need to find some users!')

current_users = ['Cassie', 'Jordan', 'John', 'Michael', 'Bob']
new_users     = ['Peter', 'Smith', 'Patrick', 'Bob', 'Michael']

for new_user in new_users:
    if new_user in current_users:
        print('Username already taken, please select another one')
    else:
        print('Username is available')

ordinal_number_list = list(range(1, 10))

for ordinal_number in ordinal_number_list:
    if ordinal_number == 1:
        print("1st")
    elif ordinal_number == 2:
        print("2nd")
    elif ordinal_number == 3:
        print("3rd")
    else:
        print(f"{ordinal_number}th")
